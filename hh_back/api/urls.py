from django.urls import path
from api.views import *

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:pk>', company_detail),
    path('companies/<int:pk>/vacancies', company_vacation),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:pk>', vacancy_detail),
    path('vacancies/top_ten', vacancy_top_ten),
    path('', start)
]