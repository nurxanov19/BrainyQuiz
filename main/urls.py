from .views import index, add_test, quiz, quizzes, check_test, add_question

from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('quiz/<int:test_id>/', quiz, name='quiz'),
    path('quizzes', quizzes, name='quizzes'),
    path('add-test', add_test, name='add-test'),

    path('check-test/<int:check_test_id>/', check_test, name='check-test'),
    path('add-question/<int:test_id>/', add_question, name='add-question'),

]