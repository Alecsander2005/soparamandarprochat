from django.urls import path
from . import views

app_name = 'imagem'

urlpatterns = [
    path('remover/<int:pk>', views.ImagensDeleteView.as_view(), name='remover'),
    path('detalhe/<int:pk>', views.ImagensDetailView.as_view(), name='detalhe'),
    path('atualizar/<int:pk>', views.ImagensUpdateView.as_view(), name='atualizar'),
    path('cadastrar', views.ImagensCreateView.as_view(), name='cadastro'),
    path('listar', views.ImagensListView.as_view(), name='listar'),

]

# Idealmente coloca-se os paths mais elaborados primeiro, e os mais simples depois.
# Para poder acessar a url no template é importante definir o app_name.
# para acessar o nome da view no template é importante definir o name.
# Esse acesso é feito com a função {% url 'app_name:name' %}
