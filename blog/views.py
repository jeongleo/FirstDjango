from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

# CBV 구현

class PostList(ListView):
    model = Post
    ordering = '-pk'
    
    ## ListView는 object_list라는 이름을 가진 템플릿 파일을 쓴다.
    ## 다른 이름을 쓰려면 아래와 같이 선언해주어야 한다.
    # template_name = 'blog/index.html' 

class PostDetail(DetailView):
    model = Post

## FBV 구현

#from django.shortcuts import render

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
    
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts' : posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
    
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post,
#         }
#     )
