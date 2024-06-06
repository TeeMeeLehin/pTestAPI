from django.shortcuts import render, redirect
from .forms import (
    PersonalityTestForm,
    InterestSelectionForm,
    AbilitySelectionForm,
    LearningInterestForm,
)
from .models import DLLQuestion
from .utils import web_dll, web_perse, compute_query, recommend_courses


def index(request):
    return render(request, "test/index.html")


def personality_view(request):
    if request.method == "POST":
        form = PersonalityTestForm(request.POST)

        if form.is_valid():

            selected_option_tags = [
                option_tag for _, option_tag in form.cleaned_data.items()
            ]
            request.session["ptest_responses"] = selected_option_tags

            return redirect("dll")
    else:
        form = PersonalityTestForm()

    return render(request, "test/personality.html", {"form": form})


def dll_view(request):
    questions = DLLQuestion.objects.all()
    score = 0

    if request.method == "POST":
        for question in questions:
            selected_option_id = request.POST.get(f"question_{question.id}", None)

            if selected_option_id:
                selected_option = question.options.get(id=selected_option_id)
                score += selected_option.option_value / 4

            dll_texts = web_dll(score)
            request.session["dll_level"] = [dll_texts[0], dll_texts[1]]

        return redirect("abilities")

    return render(request, "test/dll.html", {"questions": questions})


def abilities_view(request):
    if request.method == "POST":
        form = AbilitySelectionForm(request.POST)
        if form.is_valid():
            selected_abilities = form.cleaned_data["selected_abilities"]
            request.session["abilities"] = selected_abilities
            return redirect("wants")

    else:
        form = AbilitySelectionForm()

    return render(request, "test/ability.html", {"form": form})


def learning_interest(request):
    if request.method == "POST":
        form = LearningInterestForm(request.POST)
        if form.is_valid():
            wants = form.cleaned_data["learning_interest"]
            request.session["wants"] = wants
            return redirect("recommend")
    else:
        form = LearningInterestForm()
    return render(request, "test/wants.html", {"form": form})


def recommend(request):
    query = compute_query(request.session)
    courses = recommend_courses(query)
    
    return render(request, 'test/recommend.html', {'courses': courses})

"""
def interests_view(request):
    if request.method == "POST":
        form = InterestSelectionForm(request.POST)
        if form.is_valid():

            selected_interests = form.cleaned_data["selected_interests"]
            request.session["interests"] = selected_interests

            return redirect("results")

    else:
        form = InterestSelectionForm()

    return render(request, "test/interest.html", {"form": form})


def results(request):
    ptest = web_perse(request.session.get("ptest_responses", []))
    dll = request.session.get("dll_level", [])
    interests = request.session.get("interests", [])

    return render(
        request,
        "test/results.html",
        {"ptest": ptest, "dll": dll, "interests": interests},
    )
"""
