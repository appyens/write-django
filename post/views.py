from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import F
from django.http.response import HttpResponse

from .models import Post, Comment
from .forms import AddCommentForm, EmailForm


def home(request):

    latest_posts = Post.objects.filter(status='published').order_by('-publish')[:3]
    popular_posts = Post.objects.all().order_by('-views')[:3]

    return render(request, 'post/home.html', {'posts': latest_posts, 'popular': popular_posts})


def post_list(request):

    posts = Post.objects.filter(status='published')
    popular_posts = Post.objects.all().order_by('-views')[:3]
    paginator = Paginator(object_list=posts, per_page=2)  # Show 25 contacts per page.
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    return render(request, 'post/post_list.html', {'page_obj': page_obj, 'popular': popular_posts})


def post_detail(request, year, month, day, slug):
    # try:
    #     post = Post.objects.get(slug=post_slug)
    # except Post.DoesNotExist as err:
    #     pass

    # getting post
    post = get_object_or_404(Post, slug=slug, publish__year=year, publish__month=month, publish__day=day)
    comments = Comment.objects.filter(post=post)
    post.views = F('views') + 1
    post.save(update_fields=['views'])

    # getting related posts
    # post_tags_id = post.tags.all().values_list('id', flat=True)
    # related = Post.objects.filter(tags__in=post_tags_id).exclude(tags__in=post.tags.id)
    # final_related = related.annotate(same_tags=)

    # print(related)
    # comments
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            form = AddCommentForm()
            context = {'post': post, 'comments': comments, 'form': form, 'related_posts': None}
            return render(request, 'post/post_detail.html', context)
    else:
        form = AddCommentForm()
        context = {'post': post, 'comments': comments, 'form': form, 'related_posts': None}
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
        # post_with_title = Post.objects.filter(title__icontains=query)
        # post_with_body = Post.objects.filter(body__icontains=query)
        # final_qs = (post_with_title | post_with_body)
        result = Post.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
        )
        return render(request, 'post/post_list.html', {'result': result, 'app_name': 'post'})