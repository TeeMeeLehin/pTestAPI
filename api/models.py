from django.db import models


class PersonalityQuestion(models.Model):
    question_text = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.question_text[:50]


class PersonalityOption(models.Model):
    option_tag = models.CharField(max_length=32, null=False, blank=False)
    option_text = models.CharField(max_length=255, null=False, blank=False)
    option_res = models.CharField(max_length=500)
    question = models.ForeignKey(
        PersonalityQuestion, on_delete=models.CASCADE, related_name="options"
    )

    def __str__(self):
        return self.option_text


class DLLQuestion(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text


class DLLOption(models.Model):
    question = models.ForeignKey(
        DLLQuestion, on_delete=models.CASCADE, related_name="options"
    )
    option_text = models.CharField(max_length=255, null=False, blank=False)
    option_value = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.option_text


class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ability(models.Model):
    ability_tag = models.CharField(max_length=32, null=False, blank=False)
    ability_text = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.ability_tag}: {self.ability_text}"

    class Meta:
        verbose_name_plural = "Abilities"


class Courses(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    url = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=400, blank=False, null=False)
    level = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    review = models.CharField(max_length=100)
    tags = models.CharField(max_length=500)
    slugs = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.title
