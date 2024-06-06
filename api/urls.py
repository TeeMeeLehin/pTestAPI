from django.urls import path
from .views import (
    personality_view,
    dll_view,
    abilities_view,
    learning_interest,
    # interests_view,
    # results,
    index,
    recommend,
)

urlpatterns = [
    path("personality/", personality_view, name="personality"),
    path("dll/", dll_view, name="dll"),
    path("abilities/", abilities_view, name="abilities"),
    path("wants/", learning_interest, name="wants"),
    path("recommend/", recommend, name="recommend"),
    # path("interests/", interests_view, name="interests"),
    # path("results/", results, name="results"),
    path("", index, name="index"),
]
