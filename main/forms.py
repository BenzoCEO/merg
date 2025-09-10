from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'w-full border p-2 rounded','placeholder':'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'w-full border p-2 rounded','placeholder':'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'w-full border p-2 rounded','placeholder':'Your Message'}))
