from django.shortcuts import render

from django.shortcuts import render
from models import Blog,Comment
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime

# Create your views here.

def index(request):
    print 'hij komt bij INDEX'
    blog = Blog.objects.all()
    comment = Comment.objects.all()
    return render(request, 'blog/index.html', {'blog' : blog, 'comment':comment})

def comment(request,blog_id):
    comment = Comment.objects.all()
    return render(request, 'blog/comment.html', {'comment' : comment, 'blog_id' : blog_id})

def comment_submit(request,blog_id):
    p = Blog.objects.get(pk=blog_id)
    p.comment_set.create(comment=request.POST['comment'], pub_date = datetime.now())
    p.save()
    return HttpResponseRedirect(reverse('blog:index'))

def blog_entry(request):
    q = Blog.objects.create(blog_text=request.POST['blog_text'], pub_date = datetime.now())
    q.save()
    return HttpResponseRedirect(reverse('blog:index'))

