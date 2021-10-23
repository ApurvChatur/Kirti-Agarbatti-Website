from django.urls import path
from .views import (home_view,
                    category_view,
                    products_view,
                    product_view,
                    )


app_name = 'ProjectReal'

urlpatterns = [
    path('', home_view, name='home-page'),
    path('category/<slug:slug>/', category_view, name='category-page'),
    path('products/', products_view, name='products-page'),
    path('product/<slug:slug>/', product_view, name='product-page'),
]
