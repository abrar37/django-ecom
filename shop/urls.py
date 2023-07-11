from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('search-product/', views.search_product, name='SearchProduct'),
    path('single-product/', views.single_product, name='SingleProduct'),
    path('checkout/', views.checkout, name='Checkout'),
    path('tracking/', views.tracking, name='TrackingStatus'),
]
