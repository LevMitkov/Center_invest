from django.contrib import admin
from django.forms import inlineformset_factory
from django import forms
from .models import *


class DirectionOfTheAppealInline(admin.TabularInline):
    model = DirectionOfTheAppeal
    extra = 1
class ForeignLanguagesInline(admin.TabularInline):
    model = ForeignLanguages
    extra = 1


class EnterprisesInline(admin.TabularInline):
    model = Enterprises
    extra = 1


class FamilyRememberInline(admin.TabularInline):
    model = FamilyRemember
    extra = 1


class HigherEducationInline(admin.TabularInline):
    model = HigherEducation
    extra = 1


class DesiredDirectionInline(admin.TabularInline):
    model = DesiredDirection


class AplicationConf(admin.ModelAdmin):
    inlines = [
        DirectionOfTheAppealInline,
        FamilyRememberInline,
        EnterprisesInline,
        ForeignLanguagesInline,
        HigherEducationInline,
    ]

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
class QuestionInline(admin.StackedInline):
    inlines = [AnswerInline,]
    model = Question
    extra = 1

class TestConf(admin.ModelAdmin):
    inlines = [QuestionInline,]


class QuestionConf(admin.ModelAdmin):
    inlines = [AnswerInline,]


admin.site.register(TestResult)
admin.site.register(Test, TestConf)
admin.site.register(Question, QuestionConf)
admin.site.register(Answer)
admin.site.register(Categories)
admin.site.register(Aplication, AplicationConf)
admin.site.register(FamilyRemember)
admin.site.register(Enterprises)
admin.site.register(ForeignLanguages)
admin.site.register(HigherEducation)
admin.site.register(DirectionOfTheAppeal)
admin.site.register(DesiredDirection)