from django.urls import path
from . import views

urlpatterns = [
    # CBV 구현
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    
    # FBV 구현
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page),
]