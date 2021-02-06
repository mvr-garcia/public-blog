from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostForm


def index(request):
    """A pagina inicial de blogs como os posts em ordem cronólogica."""
    blogpost = BlogPost.objects.order_by("-date_added")
    context = {'blogpost': blogpost}
    return render(request, 'blogs/index.html', context)


@login_required()
def new_post(request):
    """Adiciona um novo post"""

    if not request.user.is_authenticated:
        raise Http404

    if request.method != 'POST':
        # Nenhum dado submetido, cria um formulário em branco
        form = BlogPostForm()
    else:
        # Dados POST submetidos; Dados processados.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blogpost = form.save(commit=False)
            new_blogpost.owner = request.user
            new_blogpost.save()
            return redirect('blogs:index')

    # Em caso de dados não submetido (IF=True),mostra um form em branco ou inválido.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required()
def edit_blogpost(request, post_id):
    """Edita um post existente"""
    blogpost = BlogPost.objects.get(id=post_id)

    # Confirma se o usuario que deseja editar é o proprietario do post
    if blogpost.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Requisição inicial; Preencha o form com o conteúdo atual, deixando disponivel para edição.
        form = BlogPostForm(instance=blogpost)
    else:
        # Dados POST submetidos; dados processados
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'blogs/edit_blogpost.html', context)
