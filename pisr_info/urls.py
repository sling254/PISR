from django.urls import path
from .views import IndexView, LandingPageView
from .import views

urlpatterns = [
    path('', LandingPageView, name='landingpage'),
    path('home/', IndexView, name='home'),
]
