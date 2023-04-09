from django import forms
from django.forms import inlineformset_factory

from .models import *


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['title', 'description']

class AplicationForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':"date", 'id':"date", 'name':"date"}))
    class Meta:
        model = Aplication
        fields = [
            'last_name', 'first_name', 'parent_name',
            'date_of_birth', 'marital_status' , 'children',
            'registration_address', 'residential_address', 'mobile_phone',
            'home_phone', 'email_address', 'average_perfomance', 'academic_degrees',
            'training_courses', 'professional_skills', 'software', 'FIO',
            'work_place', 'position_of_recom', 'phone_of_recom', 'comment',
                  ]



FamilyRememberFormSet = inlineformset_factory(Aplication, FamilyRemember,
                                              fields=('pos_in_family', 'FIO',
                                                      'date_of_birth_fanily', 'place_of_work'),
                                              extra=1, can_delete=False)
EnterprisesFormSet = inlineformset_factory(Aplication, Enterprises,
                                           fields=('title_ent', 'date_of_dismissal',
                                                   'post_ent', 'responsibilities',
                                                   'reason_of_leaving'),
                                           extra=1, can_delete=False)

class ForeignLanguagesForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = ForeignLanguages
        fields = ('title', 'proficiency_level')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title-foreign'}),
        }

ForeignLanguagesFormSet = inlineformset_factory(Aplication, ForeignLanguages,
                                                fields=('title', 'proficiency_level'),
                                                extra=1, form=ForeignLanguagesForm, can_delete=False)
HigherEducationFormSet = inlineformset_factory(Aplication, HigherEducation,
                                               fields=('name_of_the_university', 'year_of_entry',
                                                       'year_of_graduation', 'faculty',
                                                       'specialization',
                                                       'faculty', 'form_of_training'),
                                               extra=1, can_delete=False)

class DirectionOfTheAppealForm(forms.ModelForm):
    working_in_bank = forms.ChoiceField(choices=((True, 'Да'), (False, 'Нет')),label='Хотите ли работать в банке', widget=forms.RadioSelect)
    class Meta:
        model = DirectionOfTheAppeal
        fields = ('purpose', 'desired_region',
                  'date_with', 'date_before',
                  'working_in_bank', 'desired_direction',
                  'expectations', 'removal', 'documents_before',
                  'results_of_documents')
        widgets = {
            "desired_region": forms.RadioSelect(),
            'desired_direction': forms.CheckboxSelectMultiple(),
        }


DirectionOfTheAppealFormSet = inlineformset_factory(Aplication, DirectionOfTheAppeal,
                                                    fields=('purpose', 'desired_region',
                                                            'date_with', 'date_before',
                                                            'working_in_bank', 'desired_direction',
                                                            'expectations', 'removal', 'documents_before',
                                                            'results_of_documents'),
                                                    extra=1,
                                                    form=DirectionOfTheAppealForm,
                                                    can_delete=False
                                                    )


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('category',)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('test', 'question_text', 'true_answer',)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('question', 'answer_option',)


# class TestQuestionAnswerForm(forms.Form):
#     test = forms.ModelChoiceField(queryset=Test.objects.all(), label='Тест')
#     question = forms.ModelChoiceField(queryset=Question.objects.all(), label='Вопрос')
#     answer_option = forms.CharField(max_length=100, label='Вариант ответа', required=False)
#
#     def init(self, *args, **kwargs):
#         super(TestQuestionAnswerForm, self).init(*args, **kwargs)
#         if 'test' in self.initial:
#             self.fields['question'].queryset = Question.objects.filter(test=self.initial['test'])
#             self.fields['answer_option'].label = ''
#             self.fields['answer_option'].widget = forms.TextInput(attrs={'placeholder': 'Введите свой вариант ответа'})


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'