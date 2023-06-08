from django.shortcuts import render
from store.models import Product

# Create your views here.
def home_view(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request=request, template_name='./ecommerce/home.html', context=context)