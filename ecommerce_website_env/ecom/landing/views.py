# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    products = Producto.objects.all()
    template = "index.html"
    context = {
        "products": products
    }
    return render(request, template, context)
