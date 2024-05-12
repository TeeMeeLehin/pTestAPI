from ninja import NinjaAPI
from .schemas import *
from .models import *

app = NinjaAPI()

@app.get("/pq/", response=list[PQSchema])
def get_questions(request):
    questions = PersonalityQuestion.objects.all()
    return questions

@app.get("/dq/", response=list[DLLQuestionSchema])
def get_dll_questions(request):
    questions = DLLQuestion.objects.all()
    return questions

@app.get("/interests/", response=list[InterestSchema])
def get_interests(request):
    interests = Interest.objects.all()
    return interests
