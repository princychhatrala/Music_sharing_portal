from django.urls import path
from . import views

app_name = 'Music'

urlpatterns = [
    path('upload/', views.upload_music_file, name='upload-music'),
    path('private_list/', views.private_music_list, name='private-music-list'),
    path('protected_list/', views.protected_music_list, name='protected-music-list'),
]