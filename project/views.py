from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from django.views.generic.list import ListView
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import RegisterForm
from .models import Film, UserFilms
from .utils import get_max_order, reorder


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
    model = UserFilms
    paginate_by = 15
    context_object_name = 'films'

    def get_template_names(self):
        if self.request.htmx:
            return 'partials/film_list_elements.html'
        return 'films.html'
        
    def get_queryset(self):
        return UserFilms.objects.filter(user=self.request.user)

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")
    else:
        return HttpResponse("This username is available")

@login_required
def add_film(request):
    film_name = request.POST.get('film_name')
    film = Film.objects.get_or_create(name=film_name)[0]
    if not UserFilms.objects.filter(film=film, user=request.user).exists():
        UserFilms.objects.create(film=film, user=request.user, order=get_max_order(request.user))
    films = UserFilms.objects.filter(user=request.user)
    messages.success(request, f"Added {film_name} to list of films")
    return render(request, 'partials/film_list.html', {'films':films})

@login_required
@require_http_methods(['DELETE'])
def delete_film(request, id):
    UserFilms.objects.get(id=id).delete()
    reorder(request.user)
    films = UserFilms.objects.filter(user=request.user)
    return render(request, 'partials/film_list.html', {'films':films})

@login_required
def search_film(request):
    search_text = request.POST.get('search')

    user_films = UserFilms.objects.filter(user=request.user)
    results = Film.objects.filter(name__icontains=search_text).exclude(
        name__in=user_films.values_list('film__name', flat=True)
    )
    context = {"results": results}
    return render(request, 'partials/search_results.html', context)

@login_required
def detail(request, id):
    user_film = get_object_or_404(UserFilms, id=id)
    context = {"user_film": user_film}
    return render(request, 'partials/film_detail.html', context)

@login_required
def films_partial(request):
    films = UserFilms.objects.filter(user=request.user)
    return render(request, 'partials/film_list.html', {'films': films})

@login_required
def upload_photo(request, id):
    user_film = get_object_or_404(UserFilms, id=id)
    photo = request.FILES.get('photo')
    user_film.film.photo.save(photo.name, photo)
    context = {"user_film": user_film}
    return render(request, 'partials/film_detail.html', context)



def clear(request):
    return HttpResponse("")

def sort(request):
    films_ids_order = request.POST.getlist('film_order')
    films = []
    for index, film_id in enumerate(films_ids_order, start=1):
        user_film = UserFilms.objects.get(id=film_id)
        user_film.order = index
        user_film.save()
        films.append(user_film)
    return render(request, 'partials/film_list.html', {'films': films})


