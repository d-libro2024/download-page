from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .forms import EmailRegistrationForm, FileUploadForm
from .models import Book, EmailRegistration
from .models import DownloadableFile
from django.contrib import messages

def register_email(request, book_slug):
    # Retrieve the book by slug
    book = get_object_or_404(Book, slug=book_slug)

    if request.method == 'POST':
        form = EmailRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if the email is already registered for this book
            if EmailRegistration.objects.filter(email=email, book=book).exists():
                messages.info(request, "You are already registered for this book!")  # Add feedback
                return redirect('book_files', book_slug=book.slug)

            # Save the new registration
            registration = form.save(commit=False)
            registration.book = book
            registration.save()

            messages.success(request, "Registration successful! Access your downloads.")  # Add feedback
            return redirect('book_files', book_slug=book.slug)
        else:
            print("Form is invalid. Errors:", form.errors)
    else:
        form = EmailRegistrationForm()

    return render(request, 'register.html', {'form': form, 'book': book})
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

def file_list(request):
    files = DownloadableFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

def book_files(request, book_slug):
    # Retrieve the book by slug
    book = get_object_or_404(Book, slug=book_slug)
    # Get all files associated with the book
    files = DownloadableFile.objects.filter(book=book)
    return render(request, 'book_files.html', {'book': book, 'files': files})