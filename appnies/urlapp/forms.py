from . models import url_model
from django import forms


class url_forms(forms.ModelForm):
    class Meta:
        model=url_model
        fields='__all__'
