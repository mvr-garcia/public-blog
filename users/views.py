from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registra um novo usuário"""
    if request.method != 'POST':
        # Mostra um novo formulario em branco
        form = UserCreationForm()
    else:
        # Formulario processado
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Registra o usuário e redireciona para a página inicial
            login(request, new_user)
            return redirect('blogs:index')

    # Mostra o formulario branco ou invalido
    context = {'form': form}
    return render(request, 'registration/register.html', context)
