from django.conf.urls import url
from . import views

app_name = 'cadastro'

urlpatterns = [
url(r'cadastro',views.index,name='index'),
]