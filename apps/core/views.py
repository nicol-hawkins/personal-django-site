from django.shortcuts import render

def about_me(request):
    context = {}
    return render(request, 'pages/about.html', context)
    

def resume(request):
    context = {}
    return render(request, 'pages/resume.html', context)


def projects(request):
    context = {}
    return render(request, 'pages/projects.html', context)

