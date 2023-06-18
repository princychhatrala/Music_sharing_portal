from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def upload_music_file(request):
    if request.method == 'POST':
        form = MusicFileForm(request.POST, request.FILES)
        if form.is_valid():
            music_file = form.save(commit=False)
            music_file.uploaded_by = request.user
            music_file.save()
            return redirect('Music:home')
    else:
        form = MusicFileForm()
    return render(request, 'Music/upload_music_file.html', {'form': form})


@login_required
def private_music_list(request):
    music_files = Album.objects.filter(user=request.user, is_private=True)
    return render(request, 'Music/music_list.html', {'music_files': music_files})


@login_required
def protected_upload_music(request):
    if request.method == 'POST':
        form = ProtectedMusicFileForm(request.POST, request.FILES)
        if form.is_valid():
            music_file = form.save(commit=False)
            access_emails = form.cleaned_data['access_emails']
            email_list = [email.strip() for email in access_emails.split(',') if email.strip()]
            music_file.access_emails = ",".join(email_list)
            music_file.save()
            return redirect('Music:music-list') 
    else:
        form = ProtectedMusicFileForm()
    
    return render(request, 'Music/protected_upload_music.html', {'form': form})


@login_required
def protected_music_list(request):
    music_files = Album.objects.filter(is_protected=True, access_emails__contains=request.user.email)
    return render(request, 'Music/music_list.html', {'music_files': music_files})