from django.contrib import admin
from .models import Category, Test, Question

class QuestionInline(admin.TabularInline):
    model = Question


class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInline,]
    list_display = ['title', 'author']

admin.site.register(Category)
admin.site.register(Test, TestAdmin)
admin.site.register(Question)