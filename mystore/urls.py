from django.urls import path, include
from .views import ProductListView, ProductDetailView
from . import views


urlpatterns =[
    path('', ProductListView.as_view(), name='store'),
    path('<int:pk>/', ProductDetailView.as_view(), name ='product_detail'),  
    path('cart/', views.cart, name="cart"),
   
]
