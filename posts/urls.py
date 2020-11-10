from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.list, name='list'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/reorder/', views.reorder, name='reorder'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
]