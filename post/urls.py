from django.urls import path
from .views import (
    create_post,
    update_post,
    post_details_view,
    delete_post,
)

app_name = 'post'
urlpatterns = [
    path('post-details/<int:pk>/', post_details_view, name='post_details'),
    path('create-post', create_post, name='create_post'),
    path('update-post/<int:pk>/', update_post, name='update_post'),
    path('delete-post/<int:pk>/', delete_post, name='delete_post'),
]
