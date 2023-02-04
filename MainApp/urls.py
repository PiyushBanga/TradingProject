from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.handle_upload_file, name='handle_upload_file'),
]
