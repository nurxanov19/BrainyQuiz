from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Test(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True, null=True)
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

    true_answer = models.CharField(max_length=200, help_text='E.x: a ')

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


class CheckQuestion(models.Model):
    checktest = models.ForeignKey(CheckTest, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    given_answer = models.CharField(max_length=1, help_text='E.x: a')
    true_answer = models.CharField(max_length=1, help_text='E.x: a')
    is_true = models.BooleanField(default=False)


@receiver(pre_save, sender=CheckQuestion)   # javob to'g'ri berilganda is_true ni avtomatic true qilib qo'yadi
def check_answer(sender, instance, *args, **kwargs):

    print(f"Checking: {instance.given_answer} == {instance.true_answer}")

    if not instance.true_answer:
        instance.true_answer = instance.question.true_answer

    if instance.given_answer.strip().lower() == instance.true_answer.strip().lower():
        instance.is_true = True
        print("✅ Correct answer! Marking is_true = True")
    else:
        print("❌ Wrong answer!")


@receiver(post_save, sender=CheckTest)
def check_test(sender, instance, *args, **kwargs):
    checktest = instance
    checktest.found_questions = CheckQuestion.objects.filter(checktest=checktest, is_true=True).count()
    try:
        checktest.percentage = int(checktest.found_questions) * 100 // CheckQuestion.objects.filter(checktest=checktest).count()
        if checktest.test.pass_percentage <= checktest.percentage:
            checktest.user_passed = True
        checktest.save()

    except: pass

