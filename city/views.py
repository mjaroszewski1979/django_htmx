from django.shortcuts import render
from .models import City, Country

def index(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'city/index.html', context)

def cities(request):
    country = request.GET.get('country')
    cities = City.objects.filter(country=country)
    context = {'cities': cities}
    return render(request, 'city/partials/cities.html', context)
