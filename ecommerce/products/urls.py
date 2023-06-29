from django.urls import path
from products.views import getProduct

urlpatterns = [
    path('<slug>/', getProduct, name='get_product')
]
