from django.shortcuts import render


def home(request):
    context = {'title': 'Welcome!'}
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
