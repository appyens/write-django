from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.exceptions import ObjectDoesNotExist
from .forms import AddCommentForm


def home(request):

    latest_posts = Post.objects.filter(status='published')[:3]
    return render(request, 'post/home.html', {'posts': latest_posts})


def post_list(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'post/post_list.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    # try:
    #     post = Post.objects.get(slug=post_slug)
    # except ObjectDoesNotExist as err:
    #     pass

    # getting post
    post = get_object_or_404(Post, slug=slug, publish__year=year, publish__month=month, publish__day=day)
    comments = Comment.objects.filter(post=post)

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
