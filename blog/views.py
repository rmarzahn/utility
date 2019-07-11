from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def post_category(request, category_slug):
    categories = Category.objects.all()
    #post = Post.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category).order_by('-published_date')
    #template = 'blog/category/post_category.html'
    #context = {'categories':categories, 'posts':posts, 'category':category}
    return render(request, 'blog/post_category.html', {'posts':posts})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required(login_url="/accounts/login/")
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def classics(request):
    return render(request, 'classics.html')

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

 
