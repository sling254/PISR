from django.urls import path
from .views import IndexView, projects
from .import views

urlpatterns = [
    path('', IndexView, name='index'),
    path('home/', views.home, name='home' ),
    path('projects/', views.projects, name='projects' )
]
