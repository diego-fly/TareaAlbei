from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render

********** NOMBRE DE LA VISTA **************
def inicio(request):
    return render(request,'index.htm')