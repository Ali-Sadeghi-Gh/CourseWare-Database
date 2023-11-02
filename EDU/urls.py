from django.urls import path
from . import views

urlpatterns = [
    path('add_members/', views.add_members, name='add_members'),
]