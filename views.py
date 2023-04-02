from django.shortcuts import render
from datetime import datetime


def home(request):
    now = datetime.now()
    if 0 <= now.hour < 12:
        greeting = 'good morning'
    elif 12 <= now.hour < 18:
        greeting = 'good afternoon'
    else:
        greeting = 'good evening'
    context = {'title': 'Welcome!'}, {'greeting': greeting}
    return render(request, 'home.html', context)


def about(request):
    context = {'title': 'About Me'}
    return render(request, 'about.html', context)


def projects(request):
    context = {'title': 'Projects'}
    return render(request, 'projects.html', context)


def certifications(request):
    context = {'title': 'Certifications'}
    return render(request, 'certifications.html', context)


def references(request):
    context = {'title': 'References'}
    return render(request, 'references.html', context)


def contact(request):
    context = {'title': 'Contact Me'}
    return render(request, 'contact.html', context)
