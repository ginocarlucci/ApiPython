# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from TpPythonApp.models import Producto,Precio,Categoria,Empresa
from TpPythonApp.serializers import ProductoSerializer,PrecioSerializer,CategoriaSerializer
from django.shortcuts import render
from rest_framework.exceptions import NotFound

# Create your views here.
class JSONResponse(HttpResponse):
    """
    muestra la respuesta en json
    """
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)
def producto_list(request,codigoEmpresa):
    """
    lista todos los productos junto a su categoria, stock y su precio.
    :return: todos los productos
    """
    empresa = Empresa.objects.filter(codigo=codigoEmpresa)
    if request.method == 'GET' and empresa:
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto,many=True)
        return JSONResponse(serializer.data)
        """productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return JSONResponse(serializer.data)"""
    elif request.method == 'POST':
        #no necesitamos que nadie envie peticiones a nuestra  api por el momento
        return None

def producto_detalle(request,pk,codigoEmpresa):
    """
    obtener un solo producto
    :param pk: id del producto
    :return: el producto
    """
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return HttpResponse(status=404)
    empresa = Empresa.objects.filter(codigo=codigoEmpresa)
    if request.method == 'GET' and empresa:
        serializer = ProductoSerializer(producto)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        #no necesitamos que se pueda actualizar un elemento en estos momentos.
        return None
    elif request.method == 'POST':
        #no necesitamos que se pueda crear un elemento en estos momentos
        return None
    elif request.method == 'DELETE':
        #no permitimos que los usuarios borren elementos de nuestra BD
        return None


def categoria_list(request):
    """
    lista todos los productos junto a su categoria, stock y su precio.
    :return: todos los productos
    """
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        #no necesitamos que nadie envie peticiones a nuestra  api por el momento
        return None

def precios_list(request):
    """
    lista todos los productos junto a su categoria, stock y su precio.
    :return: todos los productos
    """
    if request.method == 'GET':
        precios = Precio.objects.all()
        serializer = PrecioSerializer(precios,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        #no necesitamos que nadie envie peticiones a nuestra  api por el momento
        return None