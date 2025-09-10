from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def media(request):
    return render(request, 'media.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Build email content
            subject = f"New Contact Form Submission from {name}"
            body = f"""
            You have received a new message:

            From: {name}
            Email: {email}

            Message:
            {message}
            """

            # Send the email
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                ['benardodey57@gmail.com'],  # your receiving email
                fail_silently=False,
            )

            # ✅ Redirect to success page
            return redirect('success')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')




