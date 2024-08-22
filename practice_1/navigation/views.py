from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'outer_navigation.html',)
def contact(request):
    return render(request, 'navigation/contact.html',)
def about(request):
    return render(request, 'navigation/about.html',)