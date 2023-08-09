from django.shortcuts import render
from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("Welcome to the Greetings App!")


def greet_user_view(request, username):
    return HttpResponse(f"Hello, {username}!")


def farewell_user_view(request, username):
    return HttpResponse(f"Goodbye, {username}!")
