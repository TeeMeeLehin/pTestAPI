from django.urls import path
from .views import personality_view, dll_view, interests_view, results, index

urlpatterns = [
    path("personality/", personality_view, name="personality"),
    path("dll/", dll_view, name="dll"),
    path("interests/", interests_view, name="interests"),
    path("results/", results, name="results"),
    path("", index, name="index"),
]
