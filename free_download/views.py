# free_download/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import EmailRegistrationForm, FileUploadForm
from .models import EmailRegistration
from .models import DownloadableFile

from django.shortcuts import render, redirect
from .forms import EmailRegistrationForm
from .models import EmailRegistration

def register_email(request):
    if request.method == 'POST':
        form = EmailRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if the email already exists
            if EmailRegistration.objects.filter(email=email).exists():
                # Redirect to file list if email exists
                return redirect('/files/')
            else:
                # Save the email if not already registered
                form.save()
                return render(request, 'success.html', {'download_url': '/files/'})
        else:
            # Handle case when form is invalid (e.g., unique constraint error)
            email = request.POST.get('email')
            if EmailRegistration.objects.filter(email=email).exists():
                # Redirect for existing email
                return redirect('/files/')
    else:
        form = EmailRegistrationForm()

    return render(request, 'register.html', {'form': form})

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

