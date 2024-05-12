from ninja import NinjaAPI
from .schemas import *
from .models import *
from django.http import JsonResponse

app = NinjaAPI()

@app.get("/pq/", response=list[PQSchema])
def get_questions(request):
    questions = PersonalityQuestion.objects.all()
    return questions

@app.post("/pq-submit/", response=List[ResponseSchema])
def submit_ptest(request, data: List[ResponseSchema]):
    for datum in data:
        question_id = datum.question_id
        option_id = datum.option_id
    
        try:
            question = PersonalityQuestion.objects.get(id=question_id)
            selected_option = question.options.get(id=option_id)
        except PersonalityQuestion.DoesNotExist:
            return JsonResponse({"message": "Question does not exist"}, status=404)
        except PersonalityOption.DoesNotExist:
            return JsonResponse({"message": "Option does not exist"}, status=404)
    return JsonResponse({"message": "Response submitted successfully"})


@app.get("/dq/", response=list[DLLQuestionSchema])
def get_dll_questions(request):
    questions = DLLQuestion.objects.all()
    return questions

@app.get("/interests/", response=list[InterestSchema])
def get_interests(request):
    interests = Interest.objects.all()
    return interests
