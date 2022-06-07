from django.shortcuts import render

# Create your views here.
def mostrarcomida(request):
    return render(request, "restaurante.html")