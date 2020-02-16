from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
import datetime

#Create your views here.
from django.views.generic import (ListView, DetailView,CreateView,UpdateView,DeleteView)

from Blog.models import post


def about(r):
    return render(r,'Blog/About.html',{'title':'kiran'})


class postlistview(ListView):
    model=post
    context_object_name = 'posts'
    template_name = 'Blog/Home.html'
    ordering=['-Date_Posted']
    paginate_by = 5



class postdetailview(DetailView):
    model = post
    context_object_name ='posts'
    template_name = 'Blog/post_detail.html'

class postcreateview(LoginRequiredMixin,CreateView):
    model= post
    template_name = 'Blog/post_form.html'
    context_object_name = 'form'
    fields=['Title','Content']
    def form_valid(self, form):
        form.instance.Author=self.request.user
        return super().form_valid(form)

class postupdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=post
    fields = ['Title','Content']
    def form_valid(self, form):
        form.instance.Author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.Author:
            return True
        return False

class postdeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = post
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.Author:
            return True
        return False

class userpostlistview(ListView):
    model = post
    template_name = 'Blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ["-Date_Posted"]
    paginate_by = 5
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return post.objects.filter(Author=user).order_by('-Date_Posted')


















