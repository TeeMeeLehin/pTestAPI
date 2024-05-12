from ninja import Schema, ModelSchema
from typing import List
from .models import (
    PersonalityQuestion,
    DLLQuestion,
    Interest,
    PersonalityOption,
    DLLOption,
)


class PersonalityOptionSchema(ModelSchema):
    class Meta:
        model = PersonalityOption
        fields = "__all__"


class PQSchema(Schema):
    id: int
    question_text: str
    options: List[PersonalityOptionSchema]


class ResponseSchema(Schema):
    question_id: int
    option_id: int

class DLLOptionSchema(ModelSchema):
    class Meta:
        model = DLLOption
        fields = "__all__"


class DLLQuestionSchema(Schema):
    id: int
    question_text: str
    options: List[DLLOptionSchema]


class InterestSchema(ModelSchema):
    class Meta:
        model = Interest
        fields = ["name"]
