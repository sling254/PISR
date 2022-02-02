from django.shortcuts import render
from .models import Blog, BlogCategory

# Create your views here.


def IndexView(request):
    return render(request, 'pisr_info/index.html')


def Blogview(request):
    return render (request, 'pisr_info/blog.html')
    
def Blogdetailsview(request,**kwargs):
    slug = kwargs.get('slug')
    context = {'object':Blog.objects.get(slug=slug)}
    return render (request, 'pisr_info/blog_details.html', context)

def projects(request):
    """View functionality for displaying projects template"""
    return render(request, 'pisr_info/projects.html')

def LandingPageView(request):
    return render(request, 'pisr_info/landingpage.html')

def Objective1View(request):
    return render(request, 'pisr_info/obj1.html')
def Objective2View(request):
    return render(request, 'pisr_info/obj2.html')
def Objective3View(request):
    return render(request, 'pisr_info/obj3.html')
def Objective4View(request):
    return render(request, 'pisr_info/obj4.html')
def Objective5View(request):
    return render(request, 'pisr_info/obj5.html')
def Objective6View(request):
    return render(request, 'pisr_info/obj6.html')
