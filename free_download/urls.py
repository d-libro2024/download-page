# free_download/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_email, name='register_email'),  # Registration page
    path('files/', views.file_list, name='file_list'),      # File list page
    path('upload/', views.upload_file, name='upload_file'),  # File upload page
]
