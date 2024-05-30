from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

"""
urlpatterns = [
    url(r'^variables/', views.VariableList, name='variableList'),
    url(r'^variablecreate/$', csrf_exempt(views.VariableCreate), name='variableCreate'),
]
"""

urlpatterns = [
    path('variables/', views.solicitar_tarjeta),
    path('variablecreate/', csrf_exempt(views.variable_create), name='variableCreate'),
    path('variablesAdmin/', views.variable_list, name='variableList'),
    path('variablesshow/', views.variable_list2, name='variablesShow')
]