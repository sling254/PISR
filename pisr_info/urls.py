from django.urls import path
from .views import IndexView
from .import views

urlpatterns = [
    path('', IndexView, name='index'),
    path('home/', views.home, name='home' )
]
