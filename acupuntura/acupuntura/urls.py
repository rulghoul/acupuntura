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
    path('add_color', tema_views.add_color.as_view(), name='add_color'),
    path('update_color/<int:pk>/', tema_views.update_color.as_view(), name='update_color'),
    path('list_color', tema_views.list_color.as_view(), name='list_color'),
]

path_imagen = [
    path('add_imagen', tema_views.add_imagen.as_view(), name='add_imagen'),
    path('update_imagen/<int:pk>/', tema_views.update_imagen.as_view(), name='update_imagen'),
    path('list_imagen', tema_views.list_imagen.as_view(), name='list_imagen'),
]

path_canales = [
    path('lista_canales', puntos_views.lista_canales.as_view(), name='lista_canales'),
    path('add_canal', puntos_views.AddCanalForm, name='add_canal'),
    path('borra_canal/<int:pk>/', puntos_views.borra_canal.as_view(), name='borra_canal'),
    path('update_canal/<int:pk>/', puntos_views.UpdateCanalForm, name='update_canal'),
    path('detalle_canal/<int:pk>/', puntos_views.detalle_canal.as_view(), name='detalle_canal'),
]

path_enfermedades = [
    path('lista_enfermedades', puntos_views.lista_enfermedades.as_view(), name='lista_enfermedades'),
    path('add_enfermedad', puntos_views.add_enfermedad.as_view(), name='add_enfermedad'),
    path('borra_enfermedad/<int:pk>/', puntos_views.borra_enfermedad.as_view(), name='borra_enfermedad'),
    path('update_enfermedad/<int:pk>/', puntos_views.update_enfermedad.as_view(), name='update_enfermedad'),
    path('detalle_enfermedad/<int:pk>/', puntos_views.detalle_enfermedad.as_view(), name='detalle_enfermedad'),
]

path_puntos = [
    path('lista_puntos', puntos_views.lista_puntos.as_view(), name='lista_puntos'),
    path('add_punto', puntos_views.add_punto.as_view(), name='add_punto'),
    path('borra_punto/<int:pk>/', puntos_views.borra_punto.as_view(), name='borra_punto'),
    path('update_punto2/<int:pk>/', puntos_views.PuntoUpdate.as_view(), name='update_punto2'),
    path('update_punto/<int:pk>/', puntos_views.PuntoUpdate2, name='update_punto'),
    path('detalle_punto/<int:pk>/', puntos_views.detalle_punto.as_view(), name='detalle_punto'),
]

path_emociones = [
    path('lista_emociones', puntos_views.lista_emociones.as_view(), name='lista_emociones'),
    path('add_emocion', puntos_views.add_emocion.as_view(), name='add_emocion'),
    path('borra_emocion/<int:pk>/', puntos_views.borra_emocion.as_view(), name='borra_emocion'),
    path('update_emocion/<int:pk>/', puntos_views.update_emocion.as_view(), name='update_emocion'),
    path('detalle_emocion/<int:pk>/', puntos_views.detalle_emocion.as_view(), name='detalle_emocion'),
]


path_elementos = [
    path('lista_elementos', puntos_views.lista_elementos.as_view(), name='lista_elementos'),
    path('add_elemento', puntos_views.add_elemento.as_view(), name='add_elemento'),
    path('borra_elemento/<int:pk>/', puntos_views.borra_elemento.as_view(), name='borra_elemento'),
    path('update_elemento/<int:pk>/', puntos_views.update_elemento.as_view(), name='update_elemento'),
    path('detalle_elemento/<int:pk>/', puntos_views.detalle_elemento.as_view(), name='detalle_elemento'),
]


path_parte_cuerpo = [
    path('lista_partes', puntos_views.lista_partes.as_view(), name='lista_partes'),
    path('add_parte', puntos_views.add_parte.as_view(), name='add_parte'),
    path('borra_parte/<int:pk>/', puntos_views.borra_parte.as_view(), name='borra_parte'),
    path('update_parte/<int:pk>/', puntos_views.update_parte.as_view(), name='update_parte'),
    path('detalle_parte/<int:pk>/', puntos_views.detalle_parte.as_view(), name='detalle_parte'),
]

path_sintomas = [
    path('lista_sintomas', puntos_views.lista_partes.as_view(), name='lista_partes'),
    path('add_sintoma', puntos_views.add_parte.as_view(), name='add_parte'),
    path('borra_sintoma/<int:pk>/', puntos_views.borra_parte.as_view(), name='borra_parte'),
    path('update_sintoma/<int:pk>/', puntos_views.update_parte.as_view(), name='update_parte'),
    path('detalle_sintoma/<int:pk>/', puntos_views.detalle_parte.as_view(), name='detalle_parte'),
]

path_carga_automatica = [
    path('carga_automatica', puntos_views.lista_partes.as_view(), name='lista_partes'),
]

urlpatterns = [
    path('', tema_views.home_view, name='home'),    
    #path('accounts/profile/', tema_views.home_view, name='profile'),
    path('login/', tema_views.CustomLoginView.as_view(), name='login'),
    path('logout/', tema_views.CustomLogoutView.as_view(), name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name="password_change"),    
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('admin/', admin.site.urls),
    #path('accounts/', include("django.contrib.auth.urls")), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ path_imagen   \
+ path_colores  \
+ path_canales  \
+ path_puntos   \
+ path_enfermedades   \
+ path_emociones   \
+ path_elementos   \
+ path_sintomas

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
