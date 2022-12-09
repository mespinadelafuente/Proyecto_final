from django.urls import path
from Pages import views
 
app_name = 'pages'
urlpatterns = [
    path("pages/", views.PostListView.as_view(), name="post-list"),
    path("post/add/", views.PostCreateView.as_view(), name="post-add"),
    path("post/<int:pk>/detail/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
    
    ]