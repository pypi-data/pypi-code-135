from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            message = form.cleaned_data['message']


            html = render_to_string('contact_email.html', {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'address': address,
                'message': message
            })

            send_mail('Testing', 'This is testing message','noreply@gmail.com',['ajaya.carkey890@gmail.com'], html_message=html)
            form.save()
            return redirect('success')

    else:
        form = ContactForm()

    context = {
        'form': form
    }
    
    # return HttpResponse('This is working')
    return render(request, 'index.html', context)


def success(request):
    return render(request, 'thankyou.html')
