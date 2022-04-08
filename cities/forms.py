from django import forms
from models import City


class CityForm(forms.Form):
    class Meta:
        model = City
        fields = ["name", "population"]