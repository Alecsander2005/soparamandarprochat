from django.urls import path, include
from . import views

app_name = 'exemplo'

urlpatterns = [
    path('atualizar/<int:pk>', views.ExemploUpdateView.as_view(), name='atualizar'),
    path('remover/<int:pk>', views.ExemploDeleteView.as_view(), name='remover'),
    path('<int:pk>', views.ExemploDetailView.as_view(), name='detalhe'),
    path('cadastrar', views.ExemploCreateView.as_view(), name='cadastro'),
    path('listar', views.ExemploListView.as_view(), name='listar'),
    path('datatable', views.ExemploDatatableView.as_view(), name='datatable'),
]


# Idealmente coloca-se os paths mais elaborados primeiro, e os mais simples depois.
# Para poder acessar a url no template é importante definir o app_name.
# para acessar o nome da view no template é importante definir o name.
# Esse acesso é feito com a função {% url 'app_name:name' %}
