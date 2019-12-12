# from django.conf.urls import url
from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
app_name = 'cadastro'


urlpatterns = [
# path('',views.Home.as_view(),name='home'),
path('',views.upload,name='upload'),
path('importar/',views.upload,name='upload')
# path(r'',views.inputting,name='inputting'),
# path('admin/cadastro/review/',views.upload_file,)
# path('admin/cadastro/review/',views.review,name='review')
]
