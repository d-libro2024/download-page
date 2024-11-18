from django.contrib import admin
from .models import EmailRegistration, Book, DownloadableFile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}  # Auto-fill slug from name

@admin.register(EmailRegistration)
class EmailRegistrationAdmin(admin.ModelAdmin):
    list_display = ('email', 'book', 'registered_at')  # Show book in email registrations
    list_filter = ('book',)                            # Filter by book
    search_fields = ('email', 'book__name')            # Search by email or book

@admin.register(DownloadableFile)
class DownloadableFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'book', 'uploaded_at')  # Show the file and its associated book
    list_filter = ('book',)  # Filter by book
