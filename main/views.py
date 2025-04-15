from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def add_test(request):
    return render(request, 'add-quiz.html')

def quizzes(request):
    return render(request, 'quizzes.html')

def quiz(request):
    return render(request, 'quiz.html')

def profile(request):
    return render(request, 'registration/profile.html')
