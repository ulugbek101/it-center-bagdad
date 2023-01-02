from django.urls import path

from . import views

urlpatterns = [
    path('group-delete/', views.group_delete, name='group_delete'),
]
