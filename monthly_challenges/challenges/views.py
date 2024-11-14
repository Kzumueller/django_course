from typing import List

from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

challenge_mapping = {
    "january": "Eat wild game every day!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn a new language, practice every day!",
    "april": "Be the change you would like to see in the world!",
    "may": "Be the change you would like to see in the world!",
    "june": "Be the change you would like to see in the world!",
    "july": "Be the change you would like to see in the world!",
    "august": "Be the change you would like to see in the world!",
    "september": "Be the change you would like to see in the world!",
    "october": "Be the change you would like to see in the world!",
    "november": "Be the change you would like to see in the world!",
    "december": None,
}

months: List[str] = list(challenge_mapping.keys())

def index(request: HttpRequest):
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge(request: HttpRequest, month: str):
    if month.lower() not in challenge_mapping:
        raise Http404

    return render(request, "challenges/challenge.html", {
        "month": month,
        "challenge": challenge_mapping[month.lower()]
    })


def monthly_challenge_by_number(request: HttpRequest, month: int):
    if not (0 < month <= len(months)):
        raise Http404

    return HttpResponseRedirect(reverse("challenge_base", args=[months[month - 1]]))
