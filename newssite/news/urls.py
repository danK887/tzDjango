from django.urls import  path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('tags/<int:tag_id>/', show_tags, name='tags'),
]