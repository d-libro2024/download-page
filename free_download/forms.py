# free_download/forms.py

from django import forms
from .models import EmailRegistration, DownloadableFile

class EmailRegistrationForm(forms.ModelForm):
    class Meta:
        model = EmailRegistration
        fields = ['email']


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = DownloadableFile
        fields = ['file']
