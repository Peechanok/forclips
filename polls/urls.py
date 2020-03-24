from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:poll_id>/', views.detail, name='poll_detail'),
    path('manage/', views.manage, name='poll_manage'),
    path('create/', views.create, name='poll_create'),
    path('update/<int:poll_id>/', views.update, name='poll_update'),
    path('delete/<int:poll_id>/', views.delete, name='poll_delete'),

    path('<int:poll_id>/question/create/', views.question_create, name='question_create'),
    path('question/<int:question_id>/update/', views.question_update, name='question_update'),
]
