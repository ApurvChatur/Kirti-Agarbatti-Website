from django.shortcuts import render, get_list_or_404, get_object_or_404
from ProjectDesign.models import  (Home,
                                   Category,
                                   Product,
                                   )


def home_view(request):
    home = get_object_or_404(Home, slug='kirti-agarbatti')
    categories = get_list_or_404(Category)
    featured_products = get_list_or_404(Product, tag='featured')

    template_name = "ProjectReal/home-page.html"
    context = {
        'home': home,
        'categories': categories,
        'featured_products': featured_products
    }
    return render(request, template_name, context)


def category_view(request, slug):
    categories = get_list_or_404(Category)
    category = get_object_or_404(Category, slug=slug)

    template_name = 'ProjectReal/category-page.html'
    context = {
        'categories': categories,
        'category': category,
    }
    return render(request, template_name, context)


def products_view(request):
    categories = get_list_or_404(Category)
    products = get_list_or_404(Product)

    template_name = 'ProjectReal/products-page.html'
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, template_name, context)


def product_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    template_name = 'ProjectReal/product-page.html'
    context = {
        'product': product,
    }
    return render(request, template_name, context)





























