from django import template
from tema.models import parametros_colores, parametros_imagenes

register = template.Library()

@register.simple_tag
def get_color(nombre):
    color_resultado = parametros_colores.objects.filter(elemento=nombre).first()
    if not color_resultado:
        return "#AABVBCC"
    else:
        return color_resultado.color

@register.simple_tag
def get_imagen(nombre):
    momo = parametros_imagenes.objects.filter(title=nombre).first()
    if not momo:
        return f"No se encontro la imagen con el titulo {nombre}"
    else:
        return momo.image.url