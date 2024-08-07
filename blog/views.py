from django.shortcuts import render

posts = [
  {
    'author': 'GM7Avila',
    'title': 'My Linux Setup',
    'subtitle': "All my configurations and settings that I use on my Linux Mint",
    'content': 'First post content',
    'date_posted': 'August 7, 2024'
  },
  {
    'author': 'GM7Avila',
    'title': 'Hello World!',
    'subtitle': "My first post!",
    'content': 'Second post content',
    'date_posted': 'August 7, 2024'
  }
]

# Create your views here.
def home(request):
  context = {
    'posts': posts
  }

  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})