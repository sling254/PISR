from django.urls import path

from .views import IndexView, LandingPageView,ObjectiveView
from .import views

urlpatterns = [
    path('', LandingPageView, name='landingpage'),
    path('home/', IndexView, name='home'),
    path('objective1/', ObjectiveView, name='objective1'),
    path('projects/', views.projects, name='projects' )

]
