from django.urls import path

from .views import *

urlpatterns = [
    # path('aplication/', aplication_view, name='aplication_view'),
    path('', home, name='home'),
    # path('case/', test_case, name='case'),
    path('categories/', Categories_view, name='categories'),
    path('categories/<int:category_id>/', aplication_view, name='aplication_view'),
    path('categories/<int:category_id>/<int:aplication_id>/', success_view, name='success_view'),
    path('categories/<int:category_id>/<int:aplication_id>/test_for_<int:test_id>/', test_case, name='test')
]