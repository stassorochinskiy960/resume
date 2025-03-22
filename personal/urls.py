from django.urls import path
from .views import personal, download_file

urlpatterns = [
    path('', personal, name='personal'),
    path('download/<int:file_id>/', download_file, name='download_file'),
]