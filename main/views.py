from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, CheckQuestion, Test, CheckTest, Category
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import TestForm, QuestionForm

def count_of_questions(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    count = Question.objects.filter(test=test).count()
    return count

def index(request):
    tests = Test.objects.all()
    al_categories = Category.objects.all()
    context = {'tests': tests, 'al_categories' : al_categories}
    return render(request, 'index.html', context)

def quiz(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test=test)
    Question.objects.filter(test=test).count()

    attempts = CheckTest.objects.filter(student=request.user, test=test).count()
    # if (timezone.now() >= test.start_date and timezone.now() <= test.end_date) and attempts < test.maximum_attempts:
    if request.method == 'POST':
        checktest = CheckTest.objects.create(student=request.user, test=test)

        for question in questions:
            given_answer = request.POST[str(question.id)]
            CheckQuestion.objects.create(checktest=checktest, question=question, given_answer=given_answer)
        checktest.save()
        return redirect('check-test', checktest.id)
    context = {'questions': questions, 'test': test, 'count': len(questions)}
    return render(request, 'quiz.html', context)
    # else:
    #     return HttpResponse('Page not Found')

def check_test(request, check_test_id):
    checktest = get_object_or_404(CheckTest, id=check_test_id, student=request.user)

    check_questions = CheckQuestion.objects.filter(checktest=checktest)

    correct_count = check_questions.filter(is_true=True).count()
    wrong_count = check_questions.filter(is_true=False).count()

    context = {
        'checktest': checktest,
        'check_questions': check_questions,
        'correct_count': correct_count,
        'wrong_count': wrong_count,
    }
    return render(request, 'checktest.html', context)



def add_test(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(data=request.POST)
        if form.is_valid():
            test = form.save(request)
            return redirect('add-question',test.id)
    return render(request, 'add-quiz.html', {'t_form': form})


def add_question(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if test.author == request.user:
        form = QuestionForm()
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                form.save(test_id)
                if form.cleaned_data['submit_and_exit']:
                    return redirect('index')
                return redirect('add-question', test_id)
        return render(request, 'add_question.html', {'q_form': form, 'test': test})
    else: return HttpResponse('Somrthing went wrong')


def quizzes(request):
    tests = Test.objects.all()
    context = {'quizzes': tests, 'count': count_of_questions}
    return render(request, 'quizzes.html', context)


