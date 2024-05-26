from django.shortcuts import render, redirect
from .forms import *
from .models import * 
import mercadopago
from django.http import JsonResponse
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .serializers import *
from django.contrib import messages


def base(request):
    return render(request, 'base.html')

def index(request):
    data = {
        'productos': Producto.objects.all()
    }
    return render(request, 'index.html', data)

def contador(request):
    return render(request, 'contador.html')

def bodeguero(request):
    data = {
        'productos': Producto.objects.all()
    }
    return render(request, 'bodeguero.html', data)

def vendedor(request):
    return render(request, 'vendedor.html')

def login(request):
    return render(request, 'login.html')

def reporteMensual(request):
    return render(request, 'reporte-mensual.html')

def reportePromociones(request):
    return render(request, 'reporte-promo.html')

def pintura(request):
    return render(request, 'Materiales/pintura.html')

def herramientas(request):
    return render(request, 'Materiales/herramientas.html')

def sierra(request):
    return render(request, 'Materiales/sierra.html')

def taladro(request):
    return render(request, 'Materiales/taladro.html')

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirige a la página de inicio u otra página después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'Registration/registro.html', {'form': form})

def cart(request):
    context = {
        'MERCADOPAGO_PUBLIC_KEY': settings.MERCADOPAGO_PUBLIC_KEY,
    }
    return render(request, 'cart.html', context)



@csrf_exempt
def create_preference(request):
    if request.method == 'POST':
        try:
            sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)
            preference_data = json.loads(request.body)
            
            preference_response = sdk.preference().create({
                "items": preference_data['items'],
                "back_urls": {
                    "success": "http://localhost:8000/success",
                    "failure": "http://localhost:8000/failure",
                    "pending": "http://localhost:8000/pending"
                },
                "auto_return": "approved",
                "site_id": "MLC"  # Site ID para Chile
            })

            if 'error' in preference_response['response']:
                return JsonResponse(preference_response['response'], status=400)
            
            preference = preference_response["response"]
            return JsonResponse({'id': preference['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Crud Empleado

def agregar(request):
    data = {
        'form': EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar')
        else:
            data["form"] = formulario

    return render(request, 'Empleado/agregar.html', data )

def modificar(request, id):
    empleado = Empleado.objects.get(id=id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado modificado exitosamente')
            return redirect('listar')
        else:
            messages.error(request, 'Error al modificar empleado')
    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'Empleado/modificar.html', {'form': form})

def listar(request):
    empleados = Empleado.objects.all()
    return render(request, 'Empleado/listar.html', {'listadoemp': empleados})


def addEmp(request):
    data = {
        'form': EmpleadoForm()
    }
    
    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar')

    return render(request, 'Empleado/agregar.html', data)

def updateEmp(request, id):
    empleado = Empleado.objects.get(id=id)
    data = {
        'form': EmpleadoForm(instance=empleado)
    }
    
    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, instance=empleado, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar')
        data['form'] = formulario
    
    return render(request, 'Empleado/modificar.html', data)
    
def deleteEmp(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('listar')
# Path: core/models.py