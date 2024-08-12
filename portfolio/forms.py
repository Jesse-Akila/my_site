from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(
        widget = forms.TextInput(attrs={"placeholder": "Your e-mail"})
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    message = forms.CharField(
        widget = forms.Textarea(attrs={"placeholder": "Your message"})
    )