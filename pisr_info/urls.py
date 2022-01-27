from django.urls import path
from .views import IndexView,EngagementView

urlpatterns = [
    path('', IndexView, name='index'),
    path('engagement', EngagementView, name='engagement')
]
