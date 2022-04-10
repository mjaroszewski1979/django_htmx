from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div, InlineRadios, PrependedText, PrependedAppendedText
from crispy_forms import layout, bootstrap
from django.urls import reverse_lazy
from .models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["name", "population"]

    @property
    def helper(self):
        helper = FormHelper()

        for field in self.Meta().fields:
            helper.layout.append(
                Field(field)
            )
        
        helper.field_class = 'col-4'
        
        return helper



    