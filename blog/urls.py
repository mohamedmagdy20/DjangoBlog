from django.urls import path
from blog.views import PostDeleteView, PostUpdateView, about, home,PostListView , PostDetailView,CreatePostView
urlpatterns =[
    path('',PostListView.as_view(),name='blog_home'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post_detail'),
    path('post/new/',CreatePostView.as_view(),name='post_create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post_delete'),
    
    path('about/',about,name='blog-about')
]