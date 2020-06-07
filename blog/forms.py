from django.core.exceptions import ValidationError
from django.forms import HiddenInput
from django.forms.models import ModelForm
from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'message']


class QuestionnaireForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        required_fields = self.instance.required_fields
        hidden_fields = self.instance.hidden_fields
        for field in self.fields:
            if field in required_fields:
                self.fields.get(field).required = True
            if field in hidden_fields:
                self.fields.get(field).widget = HiddenInput()

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name", "")
        if "e" in first_name:
            raise ValidationError(
                "People with 'e' in their first name need not apply.")
        # else
        return first_name
