from django.urls import path
from . import views

urlpatterns = [
    path('save-item/', views.save_item, name='save-item'),
    path('delete-item/', views.delete_item, name='delete-item'),
]