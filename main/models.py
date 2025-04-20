from django.db import models
from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Test(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    maximum_attempts = models.PositiveBigIntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=(timezone.now()+timezone.timedelta(days=10)))
    pass_percentage = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    right_answer = models.CharField(max_length=200, help_text='E.x: a ')

    def __str__(self):
        return self.question


class CheckTest(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    found_questions = models.PositiveBigIntegerField(default=0)
    user_passed = models.BooleanField(default=0)
    percentage = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.student} - {self.percentage}"
