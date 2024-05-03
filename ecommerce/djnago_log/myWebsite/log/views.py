from django.shortcuts import render

def home(request):
    return render(request, 'log_templates/home.html', {})
