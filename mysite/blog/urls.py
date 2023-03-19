from django.urls import path
from . import views
import blog.views

urlpatterns = [
    path('base/', blog.views.base, name='base'),
    path('detail/<int:blog_id>/', blog.views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('postcreate/', views.post_create, name='postcreate'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
]
