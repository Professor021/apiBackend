from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.product_list_create, name='product-list-create'),
    # path('products/create/', views.create_product, name='crate_Products'),
    path('products/<int:pk>/edit/', views.update_product, name='update_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('categories/', views.get_categories),
]