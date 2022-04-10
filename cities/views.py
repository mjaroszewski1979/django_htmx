from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div, InlineRadios, PrependedText, PrependedAppendedText
from .models import City
from .forms import CityForm


class CityDetail(DetailView):
    template_name = 'cities/detail.html'
    
    def get_object(self):
        queryset = City.objects.all()
        self.slug = self.kwargs.get('slug')
        self.city = get_object_or_404(City, slug=self.slug)
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['city'] = self.city
        return context

class CityCreate(CreateView):
    form_class = CityForm
    template_name = 'cities/create.html'
    success_message = "New city was created successfully"


def check_name(request):
    name = request.POST.get('name')
    if City.objects.filter(name=name).exists():
        return HttpResponse("<div id='name-err' class='error'>This name already exists</div>")
    else:
        return HttpResponse("<div id='name-err' class='success'>This name is available</div>")


