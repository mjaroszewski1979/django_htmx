from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from models import City
from forms import CityForm


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
    success_url = reverse_lazy('login')
    template_name = 'cities/create.html'
    success_message = "New city was created successfully"

