from django import forms
from .models import PersonalityQuestion, Interest, Ability


class PersonalityTestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PersonalityTestForm, self).__init__(*args, **kwargs)

        # Dynamically generate form fields for each question
        for question in PersonalityQuestion.objects.all():
            choices = [
                (option.option_tag, option.option_text)
                for option in question.options.all()
            ]
            field_name = f"question_{question.id}"
            self.fields[field_name] = forms.ChoiceField(
                label=question.question_text,
                choices=choices,
                widget=forms.RadioSelect,
                required=True,
            )


class InterestSelectionForm(forms.Form):
    interests = Interest.objects.values_list("name", "name")

    selected_interests = forms.MultipleChoiceField(
        choices=interests, widget=forms.CheckboxSelectMultiple, required=False
    )


class AbilitySelectionForm(forms.Form):
    ability_choices = Ability.objects.values_list("id", "ability_text")

    selected_abilities = forms.MultipleChoiceField(
        choices=ability_choices, widget=forms.CheckboxSelectMultiple, required=False
    )


class LearningInterestForm(forms.Form):
    learning_interest = forms.CharField(
        label="What do you want to learn?", max_length=300
    )
