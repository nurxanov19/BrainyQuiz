from .views import index, add_test, quiz, quizzes
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('quiz', quiz, name='quiz'),
    path('quizzes', quizzes, name='quizzes'),
    path('add-test', add_test, name='add-test'),
]