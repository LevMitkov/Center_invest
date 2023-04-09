from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import *


def aplication_view(request, category_id):
    form = AplicationForm()
    higher_education = HigherEducationFormSet(request.POST or None, prefix='higher_education')
    family_related = FamilyRememberFormSet(request.POST or None, prefix='family_related',)
    enterpises = EnterprisesFormSet(request.POST or None, prefix='enterpises',)
    foreign = ForeignLanguagesFormSet(request.POST or None, prefix='foreign',)
    direction = DirectionOfTheAppealFormSet(request.POST or None, prefix='direction',)

    if request.method == 'POST':
        form = AplicationForm(request.POST)
        if form.is_valid() and higher_education.is_valid():
            # url_data = Aplication(id=request.POST['id'])
            aplication = form.save()
            higher_education.instance = aplication
            higher_education.save()

            if family_related.is_valid():
                family_related.instance = aplication
                family_related.save()

            if enterpises.is_valid():
                enterpises.instance = aplication
                enterpises.save()

            if foreign.is_valid():
                foreign.instance = aplication
                foreign.save()

            if direction.is_valid():
                direction.instance = aplication
                direction.save()

            # return redirect('aplication_view')
            return redirect(reverse('success_view', args=(category_id, aplication.id)))
    return render(request, 'aplication/aplication_view.html', {'form': form,
                                                               'family_related': family_related,
                                                               'enterpises': enterpises,
                                                               'foreign': foreign,
                                                               'higher_education': higher_education,
                                                               'direction': direction,
                                                               'category_id': category_id}
                  )

def success_view(request, category_id, aplication_id):
    print(category_id)
    aplication = get_object_or_404(Aplication, id=aplication_id)
    # aplication = Aplication.objects.get(pk=pk)
    return render(request, 'aplication/aplication_success.html', {'aplication': aplication,
                                                                  'category_id': category_id})

def Categories_view(request):
    all_category = Categories.objects.all()

    return render(request, 'aplication/categories.html', {'all_category': all_category})

# def test_view(request, category_id, aplication_id, test_id):
#     quest = Question.objects.filter(test=test_id)
#     form_test = TestForm()
#     return render(request, 'aplication/test_view.html', {'category_id': category_id,
#                                                          'aplication_id': aplication_id,
#                                                          'test_id': test_id,
#                                                          'form_test': form_test,
#                                                          'quest': quest})


def test_case(request, category_id, aplication_id, test_id):
    return render(request, 'aplication/test_case.html', {'category_id':category_id,
                                                         'aplication_id': aplication_id,
                                                         'test_id': test_id})
def home(request):
    return render(request, 'aplication/home.html')