"""Define padrões de URL para blogs."""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    # Página para adicionar um novo post
    path('new_post/', views.new_post, name='new_post'),
    # Página para editar um post existente
    path('edit_blogpost/<int:post_id>/', views.edit_blogpost, name='edit_blogpost'),
]

# Não ta encontrando o topico com id
# Link de cada post deve levar pra pagina de edição
