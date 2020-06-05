from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, F

from .models import Post, Comment
from .forms import AddCommentForm, EmailForm


def home(request):

    latest_posts = Post.custom.published().order_by('-publish')[:3]
    popular_posts = Post.custom.published().order_by('-views')[:3]
    return render(request, 'post/home.html', {'posts': latest_posts, 'popular': popular_posts})


def post_list(request):

    posts = Post.custom.published()
    popular_posts = Post.custom.published().order_by('-views')[:3]
    paginator = Paginator(object_list=posts, per_page=2)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    return render(request, 'post/post_list.html', {'page_obj': page_obj, 'popular': popular_posts})


def post_detail(request, year, month, day, slug):
    # getting post
    post = get_object_or_404(Post, slug=slug, publish__year=year, publish__month=month, publish__day=day)
    comments = Comment.objects.filter(post=post)
    post.views = F('views') + 1
    post.save(update_fields=['views'])

    # getting related posts
    post_tags_id = post.tags.all().values_list('id', flat=True)
    related = Post.objects.filter(tags__in=post_tags_id).exclude(id=post.id)

    # post comment
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            form = AddCommentForm()
            context = {'post': post, 'comments': comments, 'form': form, 'related_posts': related}
            return render(request, 'post/post_detail.html', context)
    else:
        form = AddCommentForm()
        context = {'post': post, 'comments': comments, 'form': form, 'related_posts': related}
        return render(request, 'post/post_detail.html', context)


def share_post(request, post_id):

    post = get_object_or_404(Post, id=post_id, status='published')

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_id = form.cleaned_data.get('to_id')
            to_name = form.cleaned_data.get('to_name')
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{to_name} ({to_id}) recommends you reading "{post.title}"'
            email_message = "Hi {name}, please check out this post {url}".format(name=to_name, url=post_url)
            send_mail(subject=subject, message=email_message, from_email='admin@myblog.com', recipient_list=[to_id,])
            messages.success(request, "Post has been shared successfully")
            return redirect(post.get_absolute_url())
        else:
            form = EmailForm()
            messages.error(request, "Please provide valid name")
            return render(request, 'post/share.html', {'form': form})
    else:
        form = EmailForm()
        return render(request, 'post/share.html', {'form': form})


def search_post(request):
    if request.method == 'GET':
        query = request.GET.get('query', None)
        result = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
        return render(request, 'post/post_list.html', {'result': result, 'app_name': 'post'})
