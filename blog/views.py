from django.shortcuts import render,get_object_or_404

from django.http import HttpRequest
from .models import ProjectBlog

def blog(request):
    projectblog = ProjectBlog.objects.order_by('-date')
    return render(request,"blog/all_blogs.html",{'projectblog':projectblog})

def detail(request,blog_id):
    blog = get_object_or_404(ProjectBlog, pk = blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})