import json
from django.core.management.base import BaseCommand
from api.models import Ability


class Command(BaseCommand):
    help = "Populate Ability model with data from a JSON file"

    def handle(self, *args, **kwargs):
        # Load JSON data from file
        with open("abilities.json", "r") as file:
            data = json.load(file)

        for ability_data in data:
            ability = Ability.objects.create(
                ability_tag=ability_data["ability_tag"],
                ability_text=ability_data["ability_text"],
            )

        self.stdout.write(self.style.SUCCESS("Data populated successfully!"))
