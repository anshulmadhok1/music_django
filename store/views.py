from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Song


def home(request):
    return render(request, 'index.html')


def render_playlist(request):
    songs_qs = Song.objects.all()
    return render(request, 'playlist.html', {'playlist': songs_qs})

@login_required
def render_myplaylist(request):
    songs_qs = Song.objects.filter(user=request.user)
    return render(request, 'my_playlist.html', {'playlist': songs_qs})


def audio_player(request):
    return render(request, 'audio_player.html')


def navbar(request):
    return render(request, 'navbar.html')


def songs(request):
    return render(request, 'songs.html')


@login_required
def upload_song(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=False)
            form.title = request.POST['title']
            new_song = form.save()
            new_song.user = request.user
            new_song.save()

            return render(request, 'add.html', {
                'form': UploadFileForm(), 'success_msg': 'song is uploaded successfully!'
            })
    else:
        return render(request, 'add.html', {'form': UploadFileForm()})
