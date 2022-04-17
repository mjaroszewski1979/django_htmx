from django.urls import path
from project import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("films/", views.FilmList.as_view(), name="film_list"),
]

hmtx_views = [
    path("check-username/", views.check_username, name='check-username'),
    path('add-film/', views.add_film, name='add_film'),
    path('delete-film/<int:id>/', views.delete_film, name='delete_film'),
    path('search-film/', views.search_film, name='search_film'),
    path('clear/', views.clear, name='clear'),
    path('sort/', views.sort, name='sort'),
    path('detail/<int:id>/', views.detail, name='detail'),
]


urlpatterns += hmtx_views