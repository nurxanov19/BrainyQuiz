from django.contrib import admin
from .models import Category, Test, Question, CheckTest, CheckQuestion
from django.contrib.auth.models import Group

class QuestionInline(admin.TabularInline):
    model = Question


class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInline,]
    list_display = ['title', 'author']

admin.site.register(Category)
admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(CheckTest)
admin.site.unregister(Group)
admin.site.register(CheckQuestion)
