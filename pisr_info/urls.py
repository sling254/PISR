from django.urls import path
from .views import IndexView, LandingPageView, EngagementView
from .import views

urlpatterns = [
    path('', LandingPageView, name='landingpage'),
    path('home/', IndexView, name='home'),
   path('engagement', EngagementView, name='engagement')

]
