from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Post

# Create your views here.
def blog_home(request):
    data = Post.objects.all()
    context = {'data':data}
    return render(request,'blog/blog.html',context)

def blog_post(request,slug):
    posts = Post.objects.filter(slug=slug).first()
    context = {'posts':posts}
    return render(request,'blog/blog_post.html',context)
