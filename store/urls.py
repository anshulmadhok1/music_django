from django.urls import path
from . import views
from . import auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('signin', auth_views.signin, name='signin'),
    path('register', auth_views.register, name='register'),
    path('logout', auth_views.logout_view, name='logout'),
    path('playlist', views.render_playlist, name='playlist'),
    path('my-playlist', views.render_myplaylist, name='my-playlist'),
    path('upload-song', views.upload_song, name='upload-song'),
    path('audio-player', views.audio_player, name='audio-player'),
    path('navbar', views.navbar, name='navbar'),
    path('songs', views.songs, name='songs'),
]
