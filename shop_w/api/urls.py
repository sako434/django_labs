from django.urls import path
from api.views import *

urlpatterns = [
    path('products/', product_list),
    path('product/<int:pk>', product_detail),
    path('category/', category_list),
    path('category/<int:pk>', category_detail),
    path('category/<int:pk>/product', categories_product),
]
