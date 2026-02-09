from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_rutinas, name='lista_rutinas'),
    path('crear/', views.crear_rutina, name='crear_rutina'),
       path('rutina/<int:rutina_id>/', views.detalle_rutina, name='detalle_rutina'),

       path('editar/<int:rutina_id>/', views.editar_rutina, name='editar_rutina'),
path('eliminar/<int:rutina_id>/', views.eliminar_rutina, name='eliminar_rutina'),
]
