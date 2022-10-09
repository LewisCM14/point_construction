from django.shortcuts import render

def index(request):
    """ render the home page """
    return render(request, 'home/index.html')