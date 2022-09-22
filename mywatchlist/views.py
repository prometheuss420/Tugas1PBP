from django.shortcuts import render
from mywatchlist.models import Movie
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_mywatchlist = Movie.objects.all()
    greeting = ""
    if len(Movie.objects.filter(is_watched = True)) >= len(Movie.objects.filter(is_watched = False)) :
        greeting = "Selamat, kamu sudah banyak menonton!"
    else:
        greeting = "Wah, kamu masih sedikit menonton!"

    context = {
    'list_watchlist': data_mywatchlist,
    'nama': 'Dito Syahputra',
    'npm' : '2106638053',
    'greet' : greeting,
    }
    return render(request, "mywatchlist.html",context)



def show_xml(request):
    data = Movie.objects.all()
    return HttpResponse(serializers.serialize("xml",data), content_type="application/xml")

def show_json(request):
    data = Movie.objects.all()
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")

def show_xml_by_id(request,id):
    data = Movie.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml",data), content_type="application/xml")

def show_json_by_id(request,id):
    data = Movie.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")