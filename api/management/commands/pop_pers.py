import json
from django.core.management.base import BaseCommand
from api.models import PersonalityQuestion, PersonalityOption


class Command(BaseCommand):
    help = "Populate PersonalityQuestion and PersonalityOption models with data from a JSON file"

    def handle(self, *args, **kwargs):
        # Load JSON data from file
        with open("personality.json", "r") as file:
            data = json.load(file)

        for question_data in data:
            question = PersonalityQuestion.objects.create(
                question_text=question_data["question"]
            )

            for option_data in question_data["options"]:
                PersonalityOption.objects.create(
                    question=question,
                    option_text=option_data["option_text"],
                    option_tag=option_data["option_tag"],
                )

        self.stdout.write(self.style.SUCCESS("Data populated successfully!"))
