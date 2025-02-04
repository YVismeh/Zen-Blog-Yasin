from django.shortcuts import render, redirect
from django.views.generic import ListView, DateDetailView
from .models import Blog
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = "blog"
    paginate_by = 2

    def get_queryset(self):
        if self.kwargs.get("category"):
            blog = self.model.objects.filter(category__title=self.kwargs.get("category"), status=True)
        elif self.kwargs.get("search"):
            search = self.request.GET.get("search")
            blog = self.model.objects.filter(title__contains=search, status=True)
        else:
            blog = Blog.objects.filter(status=True)
        return blog
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first = 1
        blog_paginate = Paginator(self.get_queryset(), 2)
        last = blog_paginate.num_pages
        context["first"] = first
        context["last"] = last
        
        return context
