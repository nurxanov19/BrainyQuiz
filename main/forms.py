from .models import Test, Question
from django import forms

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'category', 'description', 'maximum_attempts', 'start_date', 'end_date',  'pass_percentage']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'quizTitle'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'quizDescription', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-select', 'id': 'quizCategory'}),
            'pass_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'maximum_attempts': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

    def save(self, request, commit=True):
        test = super().save(commit=False)
        test.author = request.user
        if commit:
            test.save()
        return test


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'a', 'b', 'c', 'true_answer']
    submit_and_exit = forms.BooleanField(required=False)

    def save(self, test_id, commit=True):
        question = self.instance
        question.test = Test.objects.get(id=test_id)
        super().save(commit)
        return question
