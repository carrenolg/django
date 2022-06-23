from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

list_challenges = {
    "may": "May - Walk for at least 20 minutes every day!",
    "june": "June - Walk for at least 20 minutes every day!",
}

# Create your views here.
def index(request):
    list_item = ""
    months = list(list_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_item += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)

def january(request):
    return HttpResponse("Eat no met for the entire month!")

def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")

def monthly_challenge_by_number(request, month):
    months = list(list_challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    challenge_text = None
    try:
        challenge_text = list_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported!")
