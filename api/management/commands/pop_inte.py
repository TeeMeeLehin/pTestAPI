from django.core.management.base import BaseCommand
from api.models import Interest


class Command(BaseCommand):
    help = "Populates the Interest model with predefined interests"

    def handle(self, *args, **kwargs):
        interests = [
            "Programming",
            "Web Development",
            "Mobile App Development",
            "Data Science",
            "Machine Learning",
            "Artificial Intelligence",
            "Cybersecurity",
            "Digital Marketing",
            "Graphic Design",
            "UI/UX Design",
            "Product Management",
            "Project Management",
            "Business Analysis",
            "Entrepreneurship",
            "Finance",
            "Accounting",
            "Human Resources",
            "Leadership",
            "Communication Skills",
            "Public Speaking",
            "Creative Writing",
            "Content Marketing",
            "SEO (Search Engine Optimization)",
            "Social Media Marketing",
            "Video Editing",
            "Photography",
            "Music Production",
            "Game Development",
            "3D Modeling",
            "Animation",
        ]

        for interest in interests:
            Interest.objects.get_or_create(name=interest)
        self.stdout.write(self.style.SUCCESS("Interests created successfully"))
