from django import forms

from formTaskApp.models import basicForm

class formDetails(forms.ModelForm):
    class Meta:
        model = basicForm
        fields = [
            "name",
            "age",
            "phoneNumber",
            "address"
        ]