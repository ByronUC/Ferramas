from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Producto', ProductoViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('contador/', contador, name='contador'),
    path('bodeguero/', bodeguero, name='bodeguero'),
    path('vendedor/', vendedor, name='vendedor'),
    path('login/', login, name='login'),
    path('reporteMensual/', reporteMensual, name='reporteMensual'),
    path('reportePromociones/', reportePromociones, name='reportePromociones'),
    path('cart/', cart, name='cart'),
    path('registro/', registro, name='registro'),

    # Materiales
    path('herramientas/', herramientas, name='herramientas'),
    path('sierra/', sierra, name='sierra'),
    path('taladro/', taladro, name='taladro'),
    path('pintura/', pintura, name='pintura'),

    # Mercado Pago
    path('create_preference/', create_preference, name='create_preference'),

    # API
    path('api/', include(router.urls)),

    # Empleado
    path('agregar/', agregar, name='agregar'),
    path('listar/', listar, name='listar'),
    path('modificar/<int:id>/', modificar, name='modificar'),
    path('deleteEmp/<int:id>/', deleteEmp, name='deleteEmp'),  # Añade esta ruta
]
