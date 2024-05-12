import json
from django.core.management.base import BaseCommand
from api.models import DLLQuestion, DLLOption


class Command(BaseCommand):
    help = "Populate DLLQuestion and DLLOption models with data from a JSON file"

    def handle(self, *args, **kwargs):
        # Load JSON data from file
        with open("dll.json", "r") as file:
            data = json.load(file)

        for question_data in data:
            question = DLLQuestion.objects.create(
                question_text=question_data["question_text"]
            )

            for option_data in question_data["options"]:
                DLLOption.objects.create(
                    question=question,
                    option_text=option_data["option_text"],
                    option_value=option_data["option_value"],
                )

        self.stdout.write(self.style.SUCCESS("Data populated successfully!"))
