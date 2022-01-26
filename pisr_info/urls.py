from django.urls import path
from .views import IndexView,CommunicateView

urlpatterns = [
    path('', IndexView, name='index'),
    path('communicate', CommunicateView, name='communicate'),
]
