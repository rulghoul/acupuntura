from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from tema import views as tema_views
from puntos import views as puntos_views

inicio = ''

path_colores = [
    path(f'{inicio}add_color', tema_views.add_color.as_view(), name='add_color'),
    path(f'{inicio}update_color/<int:pk>/', tema_views.update_color.as_view(), name='update_color'),
    path(f'{inicio}list_color', tema_views.list_color.as_view(), name='list_color'),
]

path_imagen = [
    path(f'{inicio}add_imagen', tema_views.add_imagen.as_view(), name='add_imagen'),
    path(f'{inicio}update_imagen/<int:pk>/', tema_views.update_imagen.as_view(), name='update_imagen'),
    path(f'{inicio}list_imagen', tema_views.list_imagen.as_view(), name='list_imagen'),
]

path_canales = [
    path(f'{inicio}lista_canales', puntos_views.lista_canales.as_view(), name='lista_canales'),
    path(f'{inicio}add_canal', puntos_views.add_canal.as_view(), name='add_canal'),
    path(f'{inicio}borra_canal/<int:pk>/', puntos_views.borra_canal.as_view(), name='borra_canal'),
    path(f'{inicio}update_canal/<int:pk>/', puntos_views.update_canal.as_view(), name='update_canal'),
    path(f'{inicio}detalle_canal/<int:pk>/', puntos_views.detalle_canal.as_view(), name='detalle_canal'),
]

path_enfermedades = [
    path(f'{inicio}lista_enfermedades', puntos_views.lista_enfermedades.as_view(), name='lista_enfermedades'),
    path(f'{inicio}add_enfermedad', puntos_views.add_enfermedad.as_view(), name='add_enfermedad'),
    path(f'{inicio}borra_enfermedad/<int:pk>/', puntos_views.borra_enfermedad.as_view(), name='borra_enfermedad'),
    path(f'{inicio}update_enfermedad/<int:pk>/', puntos_views.update_enfermedad.as_view(), name='update_enfermedad'),
    path(f'{inicio}detalle_enfermedad/<int:pk>/', puntos_views.detalle_enfermedad.as_view(), name='detalle_enfermedad'),
]

path_puntos = [
    path(f'{inicio}lista_puntos', puntos_views.lista_puntos.as_view(), name='lista_puntos'),
    path(f'{inicio}add_punto', puntos_views.add_punto.as_view(), name='add_punto'),
    path(f'{inicio}borra_punto/<int:pk>/', puntos_views.borra_punto.as_view(), name='borra_punto'),
    path(f'{inicio}update_punto/<int:pk>/', puntos_views.PuntoUpdate.as_view(), name='update_punto'),
    path(f'{inicio}detalle_punto/<int:pk>/', puntos_views.detalle_punto.as_view(), name='detalle_punto'),
]

urlpatterns = [
    path(f'{inicio}', tema_views.home_view, name='home'),    
    path(f'{inicio}accounts/profile/', tema_views.home_view, name='profile'),
    path(f'{inicio}login/', tema_views.user_login, name='user_login'),
    path(f'{inicio}change-password/', auth_views.PasswordChangeView.as_view()),
    path(f'{inicio}admin/', admin.site.urls),
    path(f'{inicio}accounts/', include("django.contrib.auth.urls")), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ path_imagen   \
+ path_colores  \
+ path_canales  \
+ path_puntos   \
+ path_enfermedades