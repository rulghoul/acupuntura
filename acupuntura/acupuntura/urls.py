from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from tema.views import (user_login, home_view,add_color, update_color, list_color, add_imagen, update_imagen, list_imagen)

from puntos.views import (lista_canales, update_canal, add_canal, borra_canal, detalle_canal,
                          lista_enfermedades, update_enfermedad, add_enfermedad, borra_enfermedad, detalle_enfermedad,
                          lista_puntos, update_punto,  add_punto, 
                          borra_punto, detalle_punto, PuntoUpdate)

inicio = ''

path_colores = [
    path(f'{inicio}add_color', add_color.as_view(), name='add_color'),
    path(f'{inicio}update_color/<int:pk>/', update_color.as_view(), name='update_color'),
    path(f'{inicio}list_color', list_color.as_view(), name='list_color'),
]

path_imagen = [
    path(f'{inicio}add_imagen', add_imagen.as_view(), name='add_imagen'),
    path(f'{inicio}update_imagen/<int:pk>/', update_imagen.as_view(), name='update_imagen'),
    path(f'{inicio}list_imagen', list_imagen.as_view(), name='list_imagen'),
]

path_canales = [
    path(f'{inicio}lista_canales', lista_canales.as_view(), name='lista_canales'),
    path(f'{inicio}add_canal', add_canal.as_view(), name='add_canal'),
    path(f'{inicio}borra_canal/<int:pk>/', borra_canal.as_view(), name='borra_canal'),
    path(f'{inicio}update_canal/<int:pk>/', update_canal.as_view(), name='update_canal'),
    path(f'{inicio}detalle_canal/<int:pk>/', detalle_canal.as_view(), name='detalle_canal'),
]

path_enfermedades = [
    path(f'{inicio}lista_enfermedades', lista_enfermedades.as_view(), name='lista_enfermedades'),
    path(f'{inicio}add_enfermedad', add_enfermedad.as_view(), name='add_enfermedad'),
    path(f'{inicio}borra_enfermedad/<int:pk>/', borra_enfermedad.as_view(), name='borra_enfermedad'),
    path(f'{inicio}update_enfermedad/<int:pk>/', update_enfermedad.as_view(), name='update_enfermedad'),
    path(f'{inicio}detalle_enfermedad/<int:pk>/', detalle_enfermedad.as_view(), name='detalle_enfermedad'),
]

path_puntos = [
    path(f'{inicio}lista_puntos', lista_puntos.as_view(), name='lista_puntos'),
    path(f'{inicio}add_punto', add_punto.as_view(), name='add_punto'),
    path(f'{inicio}borra_punto/<int:pk>/', borra_punto.as_view(), name='borra_punto'),
    path(f'{inicio}update_punto/<int:pk>/', PuntoUpdate.as_view(), name='update_punto'),
    path(f'{inicio}detalle_punto/<int:pk>/', detalle_punto.as_view(), name='detalle_punto'),
]

urlpatterns = [
    path(f'{inicio}', home_view, name='home'),    
    path(f'{inicio}accounts/profile/', home_view, name='profile'),
    path(f'{inicio}login/', user_login, name='user_login'),
    path(f'{inicio}change-password/', auth_views.PasswordChangeView.as_view()),
    path(f'{inicio}admin/', admin.site.urls),
    path(f'{inicio}accounts/', include("django.contrib.auth.urls")), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ path_imagen   \
+ path_colores  \
+ path_canales  \
+ path_puntos   \
+ path_enfermedades