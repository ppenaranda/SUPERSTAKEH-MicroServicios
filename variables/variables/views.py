from .models import Variable
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import VariableForm
from .logic.variable_logic import get_variables, create_variable, get_variable_by_id
from django.urls import reverse
from django.http import JsonResponse
import json

#no tiene el auth0

def variable_list(request):
    variables = get_variables()
    context = {
        'variable_list': variables
    }
    return render(request, 'Variable/VariablesAdmin.html', context)

def solicitar_tarjeta(request):
    return render(request, 'Variable/variables.html')

def variable_create(request):
    if request.method == 'POST':
        form = VariableForm(request.POST)
        if form.is_valid():
            create_variable(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created solicitud')
            return HttpResponseRedirect(reverse('variableCreate'))
        else:
            print(form.errors)
    else:
        form = VariableForm()

    context = {
        'form': form,
    }
    return render(request, 'Variable/variableCreate.html', context)
    

def variable_list2(request):
    variables = get_variables()
    context = {
        'variable_list': variables
    }
    return render(request, 'Variable/variablesShow.html', context)