from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'leopard/index.html', context_dict)




