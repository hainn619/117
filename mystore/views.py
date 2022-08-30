from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from .models import Product, ShippingAddress, Customer, OrderItem, Order

class ProductListView(ListView):
    template_name = "store/store.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Products"] = Product.objects.all
        return context

class ProductDetailView(DetailView):
    template_name = "store/detail.html"
    model = Product

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items}
    return render(request, 'store/cart.html', context)