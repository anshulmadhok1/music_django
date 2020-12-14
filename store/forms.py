from django.forms import ModelForm
from .models import Song
from django import forms


class UploadFileForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'song']
        widgets = {
            'title': forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'Title'
              }
            ),
            'song': forms.FileInput(
                attrs={
                    'class': 'custom-file-input'
                }
            )
        }
