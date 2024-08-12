from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView  # CRUD
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post

class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html' 
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        self.user_profile = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=self.user_profile).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.user_profile
        return context


class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/post_detail.html' # <app>/<model>_<viewtype>.html

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'subtitle', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  success_url = '/'

  def test_func(self):
    post = self.get_object()
    return self.request.user == post.author
  
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title', 'subtitle', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  # Testa se o usuário é o autor do post (true/false)
  def test_func(self):
    post = self.get_object()
    return self.request.user == post.author

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})
