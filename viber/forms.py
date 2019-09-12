from django import forms
from django.forms import ModelForm
from viber.models import FAQ

class FAQForm(forms.Form):

    question = forms.CharField(widget=forms.Textarea)
    answer = forms.CharField(widget=forms.Textarea)


class FAQFormForm(ModelForm):
    class Meta:
        model = FAQ
        fields = "__all__"

