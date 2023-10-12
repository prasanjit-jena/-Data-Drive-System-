from django import forms
from .models import Folder, File
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent_folder']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter folder name (optional)'}),
        }
    # directory = forms.FileField(widget=forms.ClearableFileInput(attrs={'webkitdirectory': 'true'}))

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'parent_folder', 'file']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User  # Assuming you have imported User from django.contrib.auth.models
        fields = ['username', 'password1', 'password2']
