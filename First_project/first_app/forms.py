from django import forms

class user_form(forms.Form):
    user_name = forms.CharField(required=True,label="Full Name",initial="Mohabbat")
    user_email = forms.EmailField(required=True,label="User Email")
