from django.urls import path
from . import views  # This imports views from the current 'myapp' directory

urlpatterns = [
    path('', views.product_list, name='home'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('create/', views.create_product, name='create_product'),
    path('products/', views.product_list, name='product_list')
]