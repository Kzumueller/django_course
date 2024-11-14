from django.urls import path

from .views import monthly_challenge, monthly_challenge_by_number, index

urlpatterns = [
    path("", index, name="challenge_index"),
    path("<int:month>", monthly_challenge_by_number),
    path("<str:month>", monthly_challenge, name="challenge_base")
]
