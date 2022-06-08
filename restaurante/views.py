from django.shortcuts import render
from restaurante.models import hamburguesas
from restaurante.forms import hamburguesa_form

# Create your views here.
def mostrarcomida(request):
    return render(request, "restaurante.html")

class Create_hamburguesa(CreateView):
    model = hamburguesas
    template_name = 'create_hamburguesas.html'
    fields = '__all__'