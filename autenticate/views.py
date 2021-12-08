from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Pessoas


def add_user(request):
    if request.method == 'GET':
       return render(request, 'cadastro/index.html')
    
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        
        pessoa = Pessoas(name=name,
                    email=email,
                    senha = password)
        
        pessoa.save()
        return render(request, 'cadastro/index.html',{'status': 'success'})

def user_list(request):
    pessoas = Pessoas.objects.all()
    return render(request, 'list.html', {'users': pessoas})