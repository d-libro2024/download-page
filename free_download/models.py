import uuid
from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)  # Slug for URLs
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Automatically generate slug from name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class EmailRegistration(models.Model):
    email = models.EmailField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)  # Confirmation status
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique token

    class Meta:
        unique_together = ('email', 'book')

    def __str__(self):
        return f"{self.email} - {self.book.name}"

class DownloadableFile(models.Model):
    file = models.FileField(upload_to='downloads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)  # Default Book ID

    def __str__(self):
        return f"{self.file.name} ({self.book.name})"
