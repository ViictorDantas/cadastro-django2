from django.shortcuts import render
from .models import Usuario

def home(request):
    return render (request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    #exibir todos os usuarios ja cadastrados em uma nova pagina

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #retorna os dados para a pagina 'listagem_usuarios'
    return render (request, 'usuarios/usuarios.html',usuarios)
