from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.http import FileResponse, Http404
from .forms import EmailRegistrationForm, FileUploadForm
from .models import Book, EmailRegistration
from .models import DownloadableFile
from django.contrib import messages
from django.core.mail import send_mail
import os
from django.conf import settings
import mimetypes


def register_email(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)

    if request.method == 'POST':
        form = EmailRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if the user is already registered and confirmed
            registration = EmailRegistration.objects.filter(email=email, book=book).first()
            if registration:
                if registration.is_confirmed:
                    return redirect('book_files', book_slug=book.slug)
                else:
                    # Resend confirmation email if not confirmed
                    send_confirmation_email(registration)
                    return render(request, 'email_pending.html', {'email': email})

            # Create a new registration
            registration = form.save(commit=False)
            registration.book = book
            registration.save()

            # Send confirmation email
            send_confirmation_email(registration)
            return render(request, 'email_pending.html', {'email': email})
    else:
        form = EmailRegistrationForm()

    return render(request, 'register.html', {'form': form, 'book': book})

def send_confirmation_email(registration):
    confirmation_url = f"{settings.SITE_URL}/confirm/{registration.confirmation_token}/"
    subject = "Confirm Your Registration"
    message = f"Thank you for registering! Please confirm your email by clicking the link below:\n\n{confirmation_url}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [registration.email])

def confirm_email(request, token):
    registration = get_object_or_404(EmailRegistration, confirmation_token=token)

    if registration.is_confirmed:
        return HttpResponse("Your email is already confirmed. You can access the download page.")

    # Mark registration as confirmed
    registration.is_confirmed = True
    registration.save()

    # Redirect to the download page
    return redirect('book_files', book_slug=registration.book.slug)

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
    return render(request, 'download_list.html', {'files': files})

def book_files(request, book_slug):
    # Retrieve the book by slug
    book = get_object_or_404(Book, slug=book_slug)
    # Get all files associated with the book
    files = DownloadableFile.objects.filter(book=book)
    return render(request, 'book_files.html', {'book': book, 'files': files})

def download_file(request, file_path):
    # Construct the full file path
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)

    # Check if the file exists
    if os.path.exists(full_path):
        # Open the file
        with open(full_path, 'rb') as f:
            # Force download using 'Content-Disposition' and generic content type
            response = FileResponse(f, content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(full_path)}"'
            return response
    else:
        raise Http404("File not found.")
    

def download_file(request, file_path):
    # Construct the full file path
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)

    # Check if the file exists
    if os.path.exists(full_path):
        with open(full_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(full_path)}"'
            return response
    else:
        raise Http404("File not found.")