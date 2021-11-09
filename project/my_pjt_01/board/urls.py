from django.urls import path, include
from . import views
# from django.

app_name = 'board'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
]