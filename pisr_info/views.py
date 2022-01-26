from django.shortcuts import render

# Create your views here.


def IndexView(request):
    return render(request, 'pisr_info/index.html')


def home(request):
    return render(request, 'pisr_info/home.html')

def projects(request):
    """View functionality for displaying projects template"""
    return render(request, 'pisr_info/projects.html')