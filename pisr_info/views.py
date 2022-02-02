from django.shortcuts import render

# Create your views here.


def IndexView(request):
    return render(request, 'pisr_info/index.html')


def home(request):
    return render(request, 'pisr_info/home.html')

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
