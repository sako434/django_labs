from django.shortcuts import render
from api.models import Company, Vacancy
from django.http import JsonResponse, HttpResponse


def companies_list(request):
    companies = Company.objects.all()
    json_companies = [c.to_json() for c in companies]
    return JsonResponse(json_companies, safe=False)


def company_detail(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(company.to_json(), safe=False)


def company_vacation(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)

    vacancies = company.vacancies.all()
    json_v = [v.to_json() for v in vacancies]
    return JsonResponse(json_v, safe=False)


def vacancy_list(request):
    vacancy = Vacancy.objects.all()
    json_v = [v.to_json() for v in vacancy]
    return JsonResponse(json_v, safe=False)


def vacancy_detail(request, pk):
    try:
        vacancy = Vacancy.objects.get(id=pk)
    except vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    return JsonResponse(vacancy.to_json(), safe=False)


def vacancy_top_ten(request):
    try:
        vacancy = Vacancy.objects.all().order_by('-salary')[:10]
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)

    json_v = [v.to_json() for v in vacancy]
    return JsonResponse(json_v, safe=False)


def start(request):
    return JsonResponse('Type what you want to research', safe=False)
