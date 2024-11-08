from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BlogListView(ListView):
    model = Post
    context_object_name ='posts'
    template_name ='app/blog_list.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name ='app/blog_detail.html'
    


