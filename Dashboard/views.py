from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
import requests

def home(request):
    return render(request,'Dashboard/home.html')


