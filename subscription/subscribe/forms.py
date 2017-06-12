from django import forms	

class SubscribeForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    topics = forms.CharField(required=True)
