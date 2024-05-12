from django.contrib import admin
from .models import (
    PersonalityOption,
    PersonalityQuestion,
    Interest,
    DLLOption,
    DLLQuestion,
)

# Register your models here.
admin.site.register(PersonalityOption)
admin.site.register(PersonalityQuestion)
admin.site.register(Interest)
admin.site.register(DLLOption)
admin.site.register(DLLQuestion)
