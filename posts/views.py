from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):
    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post':post}
    return render(request, 'posts/list.html', context)

@login_required
def new(request):
    posts = Post.objects.all()
      context = {'posts': posts}
    return render(request, 'posts/new.html', context)

@login_required
def create(request):
    menu = request.POST['menu']
    stock = request.POST['stock']
    price = request.POST['price']
    order = request.POST['order']
    post = Post(menu=menu, stock=stock, price=price, order=order)
    post.save()
    return redirect('posts:list', post_id=post.id)
@login_required
def edit(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('post:index')
    context = {'post': post}
    return render(request, 'posts/reorder.html', context)

@login_required
def update(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('post:index')

    post.menu = request.POST['menu']
    post.stock = requst.models[stock]
    post.price = request.models[price] 
    post.order = request.POST['order']
    post.save()

    return redirect('posts:list', post_id=post.id)

@login_required
def delete(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('post:index')
    post.delete()

    return redirect('posts:index')
# Create your views here.
