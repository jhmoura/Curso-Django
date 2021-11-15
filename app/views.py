from django.shortcuts import render

def index(request):
    context = {
        'curso': 'Programação WEB com Django Framework', 
        'outro': 'Django é TOP!'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

