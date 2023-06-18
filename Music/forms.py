from django import forms
from .models import Album


class MusicFileForm(forms.ModelForm):
    access_emails = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text="Enter email addresses separated by commas for access"
    )

    class Meta:
        model = Album
        fields = ('title', 'file', 'is_private', 'is_public', 'is_protected', 'access_emails')


class ProtectedMusicFileForm(forms.ModelForm):
    access_emails = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text="Enter email addresses separated by commas for access"
    )
    
    class Meta:
        model = Album
        fields = ('title', 'file', 'is_protected', 'access_emails')


