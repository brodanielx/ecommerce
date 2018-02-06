from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Full Name"
                }
            )
        )
    email = forms.EmailField()
    content = forms.CharField()
