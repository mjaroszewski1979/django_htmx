from django.urls import path
from . import views

app_name = 'cities'

urlpatterns = [
    path('detail/<slug:slug>/', views.CityDetail.as_view(), name='detail'),
    path('create/', views.CityCreate.as_view(), name='create'),
]

hmtx_views = [
    path("check-name/", views.check_name, name='check_name'),
]

urlpatterns += hmtx_views