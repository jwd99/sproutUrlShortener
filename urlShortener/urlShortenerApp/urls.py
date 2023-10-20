from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('shorten', views.makeUrlShort),
    path('<str:shortUrl>', views.redirectUrl),

]