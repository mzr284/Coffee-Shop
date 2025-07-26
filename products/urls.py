from django.urls import path
from .views import CategoryListView, ProductListView, CategoryDetailView, ProductDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name="categories-view"),
    path('categories/<int:pk_category>/products/', ProductListView.as_view(), name="products-view"),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
    path('category/<str:title_category>/product/<int:pk_product>/', ProductDetailView.as_view(), name="product-detail")
]