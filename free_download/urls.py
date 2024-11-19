# free_download/urls.py

from django.urls import path
from . import views
from .views import download_file

urlpatterns = [
    path('<slug:book_slug>/', views.register_email, name='register_email'),  # Registration
    path('confirm/<uuid:token>/', views.confirm_email, name='confirm_email'),
    path('<slug:book_slug>/files/', views.book_files, name='book_files'),    # File list
    path('files/', views.file_list, name='file_list'),  # File list page
    path('upload/', views.upload_file, name='upload_file'),  # File upload page
    path('download/<path:file_path>/', download_file, name='download_file'),
]
