from django.shortcuts import render


def home(request):
    context = {'title': 'Welcome!'}
    return render(request, './templates/home.html', context)


def about(request):
    context = {'title': 'About Me'}
    return render(request, './templates/about.html', context)


def projects(request):
    context = {'title': 'Projects'}
    return render(request, './templates/projects.html', context)


def certifications(request):
    context = {'title': 'Certifications'}
    return render(request, './templates/certifications.html', context)


def references(request):
    context = {'title': 'References'}
    return render(request, './templates/references.html', context)


def contact(request):
    context = {'title': 'Contact Me'}
    return render(request, './templates/contact.html', context)
