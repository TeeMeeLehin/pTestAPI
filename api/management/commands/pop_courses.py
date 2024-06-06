import csv
from django.core.management.base import BaseCommand
from api.models import Courses


class Command(BaseCommand):
    help = "Populate the movie database with data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]
        Courses.objects.all().delete()  # Clear existing data
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Courses.objects.create(
                    title=row["Title"],
                    url=row["URL"],
                    description=row["Description"],
                    level=row["Level"],
                    status=row["Status"],
                    review=row["Review"],
                    tags=row["Tags"],
                    slugs=row["Slugs"],
                )
        self.stdout.write(
            self.style.SUCCESS("Successfully populated the courses database")
        )
