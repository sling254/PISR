from django.shortcuts import render

# Create your views here.


def IndexView(request):
    return render(request, 'pisr_info/index.html')


def LandingPageView(request):
    return render(request, 'pisr_info/landingpage.html')


def EngagementView(request):
    return render(request, 'pisr_info/engagement.html')

