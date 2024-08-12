from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView  # CRUD
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Like

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    liked = Like.objects.filter(user=request.user, post=post).exists()

    if liked:
        Like.objects.filter(user=request.user, post=post).delete()
    else:
        Like.objects.create(user=request.user, post=post)

    return redirect('post-detail', pk=post.pk)

class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html' 
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 5

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    if self.request.user.is_authenticated:
      likes = Like.objects.filter(user=self.request.user)
      liked_posts = likes.values_list('post_id', flat=True)
      context['liked_posts'] = liked_posts
    return context

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
        if self.request.user.is_authenticated:
          likes = Like.objects.filter(user=self.request.user)
          liked_posts = likes.values_list('post_id', flat=True)
          context['liked_posts'] = liked_posts
        return context

class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/post_detail.html' # <app>/<model>_<viewtype>.html

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post = self.get_object()

    # Adiciona o número total de likes no contexto
    context['total_likes'] = post.likes.count()

    if self.request.user.is_authenticated:
      context['liked'] = Like.objects.filter(user=self.request.user, post=post).exists()
    else:
      context['liked'] = False
    
    return context

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
