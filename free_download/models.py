# free_download/models.py

from django.db import models

class EmailRegistration(models.Model):
    email = models.EmailField(unique=True)  # Unique email field
    registered_at = models.DateTimeField(auto_now_add=True)  # Timestamp of registration

    def __str__(self):
        return self.email


class DownloadableFile(models.Model):
    file = models.FileField(upload_to='downloads/')  # Upload to 'media/downloads/'
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp of upload

    def __str__(self):
        return self.file.name
