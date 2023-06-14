from django.urls import path 
from . import views 

urlpatterns = [
    path("shortenurl/", views.UrlShortener.as_view())
]

