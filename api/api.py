from ninja import NinjaAPI
from .schemas import *
from .models import *
from django.http import JsonResponse
from .utils import compute_dll, compute_perse, compute_interest

app = NinjaAPI()


@app.get("/pq/", response=list[PQSchema])
def get_questions(request):
    """
    Retrieves the list of personality questions.
    
    Schema: PQSchema

    """
    questions = PersonalityQuestion.objects.all()
    return questions


@app.post("/pq-submit/", response=List[ResponseSchema])
def submit_ptest(request, data: List[ResponseSchema]):
    """
    Collects PTest Responses
    
    Schema: ResponseSchema
    """
    selected_options = []
    for datum in data:
        question_id = datum.question_id
        option_id = datum.option_id

        try:
            question = PersonalityQuestion.objects.get(id=question_id)
            selected_option = question.options.get(id=option_id)
            selected_options.append(option_id)
        except PersonalityQuestion.DoesNotExist:
            return JsonResponse({"message": "Question does not exist"}, status=404)
        except PersonalityOption.DoesNotExist:
            return JsonResponse({"message": "Option does not exist"}, status=404)
    request.session["ptest_responses"] = selected_options
    return JsonResponse({"message": "Response submitted successfully"})


@app.get("/dq/", response=list[DLLQuestionSchema])
def get_dll_questions(request):
    """
    Retrieves the list of DLL questions.
    
    Schema: DLLQuestionSchema

    """
    questions = DLLQuestion.objects.all()
    return questions


@app.post("/dq-submit/", response=List[ResponseSchema])
def submit_dlltest(request, data: List[ResponseSchema]):
    """
    Collects DLL-Test Responses.
    
    Schema: ResponseSchema
    
    """
    selected_options = []
    for datum in data:
        question_id = datum.question_id
        option_id = datum.option_id

        try:
            question = DLLQuestion.objects.get(id=question_id)
            selected_option = question.options.get(id=option_id)
            selected_options.append(option_id)
        except DLLQuestion.DoesNotExist:
            return JsonResponse({"message": "Question does not exist"}, status=404)
        except DLLOption.DoesNotExist:
            return JsonResponse({"message": "Option does not exist"}, status=404)
    request.session["dlltest_responses"] = selected_options
    return JsonResponse({"message": "Response submitted successfully"})


@app.get("/interests/", response=list[InterestSchema])
def get_interests(request):
    """
    Retrieves the list of Interests.
    
    Schema: InterestSchema

    """
    interests = Interest.objects.all()
    return interests


@app.post("/inte-submit/", response=List[IntResponseSchema])
def submit_dlltest(request, data: List[IntResponseSchema]):
    """
    Collects Interests Responses
    
    Schema: IntResponseSchema
    
    """
    selected_interests = []
    for datum in data:
        selected_interests.append(datum.interest_id)
    request.session["interests"] = selected_interests
    return JsonResponse({"message": "Response submitted successfully"})


@app.get("/results/", response=TestResultsSchema)
def test_results(request):
    """
    Retrieves the test results reponse.
    
    Schema: TestResultsSchema

    """
    ptest_responses = request.session.get("ptest_responses", [])
    dtest_responses = request.session.get("dlltest_responses", [])
    interests_responses = request.session.get("interests", [])

    dll_level = compute_dll(dtest_responses)
    ptest_out = compute_perse(ptest_responses)
    interests = compute_interest(interests_responses)

    return JsonResponse(
        {
            "ptest_output": ptest_out,
            "dlltest_output": dll_level,
            "interests_output": interests,
        }
    )
