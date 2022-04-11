from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from django.views.generic.list import ListView
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm
from .models import Film


class IndexView(TemplateView):
    template_name = 'index.html'
    
class Login(LoginView):
    template_name = 'registration/login.html'

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FilmList(LoginRequiredMixin, ListView):
    template_name = 'films.html'
    model = Film
    context_object_name = 'films'

    def get_queryset(self):
        user = self.request.user
        return user.films.all()

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")
    else:
        return HttpResponse("This username is available")

@login_required
def add_film(request):
    film_name = request.POST.get('film_name')
    film = Film.objects.create(name=film_name)
    request.user.films.add(film)
    films = request.user.films.all()
    return render(request, 'partials/film_list.html', {'films':films})

@login_required
@require_http_methods(['DELETE'])
def delete_film(request, id):
    data = Film.objects.get(id=id)
    data.delete()
    films = request.user.films.all()
    return render(request, 'partials/film_list.html', {'films':films})
