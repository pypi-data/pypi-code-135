from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    address = forms.CharField(widget=forms.TextInput())


    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','address','message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3})
        }

