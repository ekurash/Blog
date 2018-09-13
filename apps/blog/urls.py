from django.urls import path

from apps.blog.views import ListPostView, CreatePostView, UpdatePostView, DeletePostView, DetailPostView
from apps.blog.views import ListTagView, CreateTagView, UpdateTagView, DeleteTagView, DetailTagView


app_name = 'blog'


urlpatterns = [
    path(r'', ListPostView.as_view(), name='index'),
    path(r'create/', CreatePostView.as_view(), name='post-create'),
    path(r'edit<int:pk>/', UpdatePostView.as_view(), name='post-edit'),
    path(r'delete<int:pk>/', DeletePostView.as_view(), name='post-delete'),
    path(r'<int:pk>/', DetailPostView.as_view(), name='post-detail'),

    path(r'tags', ListTagView.as_view(), name='tag-index'),
    path(r'tags-create/', CreateTagView.as_view(), name='tag-create'),
    path(r'tags-edit<int:pk>/', UpdateTagView.as_view(), name='tag-edit'),
    path(r'tags-delete<int:pk>/', DeleteTagView.as_view(), name='tag-delete'),
    path(r'tags-<int:pk>/', DetailTagView.as_view(), name='tag-detail'),
]