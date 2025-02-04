from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog, Comments
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import CommentsForm

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
    

class BlogDetailsView(DetailView):
    model = Blog
    template_name = 'blog/single-post.html'

    def get_context_data(self, **kwargs):
        id = self.kwargs["pk"]
        blog = get_object_or_404(Blog, id=id)
        context = super().get_context_data(**kwargs)
        context["comments"] = Comments.objects.filter(status=True, blog=blog.id)
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                id = self.kwargs["pk"]
                blog = get_object_or_404(Blog, id=id)
                comment = form.save(commit=False)
                comment.blog = blog
                comment.save()
                messages.add_message(self.request, messages.SUCCESS, "successfully sent")
                return redirect(self.request.path_info)
            else:
                messages.add_message(request, messages.ERROR, "invalid data")
                return redirect(self.request.path_info)
        else:
            return redirect("accounts:login")
