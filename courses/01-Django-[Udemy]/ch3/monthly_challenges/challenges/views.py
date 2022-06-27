from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

list_challenges = {
    "may": "May - Walk for at least 20 minutes every day!",
    "june": "June - Walk for at least 20 minutes every day!",
    "december": None,
}

# Create your views here.
def index(request):
    months = list(list_challenges.keys())
    return render(request, "index.html", {
        "months": months
    })

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
    try:
        challenge_text = list_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("This month is not supported!")
