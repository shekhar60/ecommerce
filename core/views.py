from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Item

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'core/product.html', context)

def checkout(request):
    return render(request, 'core/checkout.html')

class HomeView(ListView):
    model = Item
    template_name = 'index.html'

    class ItemDetailView(DetailView):
        model = Item
        template_name = 'product.html'