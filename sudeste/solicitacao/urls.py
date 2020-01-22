from django.urls import path
from . import views
app_name = 'solicitacao'


urlpatterns = [
path('',views.pedidos,name='pedidos'),
path('solicitacao/',views.pedidosDetalhe,name='pedidosDetalhe'),
path('confirmacao/',views.confirmacao,name='confirmacao'),
#path('',views.index,name='index'),
# path('solicitacao/',views.opcoes,name='opcoes'),
# path('confirmacao/',views.confirmacao,name='confirmacao'),
# path('gravar/',views.gravar,name='gravar'),
]
