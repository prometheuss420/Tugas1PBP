from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_katalog,
    'nama': 'Dito Syahputra',
    'npm' : '2106638053',
    }
    return render(request, "katalog.html",context)