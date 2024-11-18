from django.contrib import admin
from .models import EmailRegistration, DownloadableFile

@admin.register(EmailRegistration)
class EmailRegistrationAdmin(admin.ModelAdmin):
    list_display = ('email', 'registered_at')

@admin.register(DownloadableFile)
class DownloadableFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
