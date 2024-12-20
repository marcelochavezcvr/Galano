#este es un archivo creado manualmente por el administrador.
#en este archivo se configuran todas las vistas de la aplicación "core".
#estas urls se van a conectar con el urls.py del proyecto global



from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path ('' , views.landing_page, name='landing_page'),
    path ('quienes_somos/' , views.quienes_somos, name ='quienes_somos'),
    path ('iniciosesion/' , views.iniciosesion, name='iniciosesion'),
    path ('tecnologias/' , views.tecnologias, name='tecnologias'),
    path ('constructora/', views.constructora, name='constructora'),
    path ('seguridad/', views.seguridad, name='seguridad'),
    path ('registro/', views.registro, name='registro'),
    path ('dashboard/' ,views.dashboard, name='dashboard'),
    path ('crear_proyecto/' , views.crear_proyecto, name = 'crear_proyecto'),
    path('eliminar_proyecto/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path ('crear_cita/' , views.crear_cita, name='crear_cita'),
    path ('eliminar_cita/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),    
]