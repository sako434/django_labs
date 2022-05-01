from django.shortcuts import render
from api.models import Product, Category
from django.http import JsonResponse,HttpResponse


def product_list(request):
    product = Product.objects.all()
    p_json = [p.to_json() for p in product]
    return JsonResponse(p_json, safe=False)


def product_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except product.DoesNotExist as e:
        JsonResponse({'error': str(e)}, safe=False)

    return JsonResponse(product.to_json(), safe=False)


def category_list(request):
    category = Category.objects.all()
    json_c = [c.to_json() for c in category]
    return JsonResponse(json_c, safe=False)


def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
        return JsonResponse(category.to_json(), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)


def categories_product(request, pk):
    try:
        category = Category.objects.get(id=pk)
        product = category.product_set.all()
    except Exception as e:
        JsonResponse({'error': str(e)}, safe=False)
    json_p = [c.to_json() for c in product]
    return JsonResponse(json_p, safe=False)
