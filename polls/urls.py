from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('index/', views.index, name='index'),
    path('detail/<int:poll_id>/', views.detail, name='poll_detail'),
]
