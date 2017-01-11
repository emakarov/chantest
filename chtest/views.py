# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

LANDING_TEMPLATE = 'chtest/index.html'

def index(request):
    return render(request, LANDING_TEMPLATE, {})

