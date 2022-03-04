from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty, Kategoria

# Create your views here.

def index(request):
    wszystkie = Produkty.objects.all()
    jeden = Produkty.objects.get(pk=6)
    kat = Produkty.objects.filter(kategoria=2)
    naz = Produkty.objects.filter(producent =1)
    kat_name = Kategoria.objects.get(id=2)
    kat_all = Kategoria.objects.all()
    null = Produkty.objects.filter(kategoria__isnull = True)
    contain = Produkty.objects.filter(opis__icontains="fon")
    kategorie = Kategoria.objects.all()
    dane = {'kategorie' : kategorie}
    return render(request,'szablon.html',dane)

def kategoria(request,id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user)

def produkt(request,id):
    produkt_user = Produkty.objects.get(pk=id)
    napis = "<h1>" + str(produkt_user) + "</h1>" + \
            "<p style='color:purple; font-size:100px;'>" + str(produkt_user.opis) + "</p>" + \
            "<p>" + str(produkt_user.cena) + "</p>"

    return HttpResponse(napis)