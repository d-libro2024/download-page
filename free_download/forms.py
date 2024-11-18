from django import forms
from .models import EmailRegistration, Book, DownloadableFile

class EmailRegistrationForm(forms.ModelForm):
    class Meta:
        model = EmailRegistration
        fields = ['email']  # Exclude 'book' from the form

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = DownloadableFile
        fields = ['file', 'book']
