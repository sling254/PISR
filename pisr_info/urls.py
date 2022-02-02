from django.urls import path

from .views import IndexView,Blogview,Blogdetailsview,LandingPageView,Objective1View,Objective2View,Objective3View,Objective4View,Objective5View,Objective6View
from .import views

urlpatterns = [
    path('', LandingPageView, name='landingpage'),
    path('blog/', Blogview, name='blog'),
    path('blog-detail/<slug:slug>/',Blogdetailsview, name="blog-detail"),
    path('objective1/', Objective1View, name='objective1'),
    path('objective2/', Objective2View, name='objective2'),
    path('objective3/', Objective3View, name='objective3'),
    path('objective4/', Objective4View, name='objective4'),
    path('objective5/', Objective5View, name='objective5'),
    path('objective6/', Objective6View, name='objective6'),
    path('projects/', views.projects, name='projects' )

]
