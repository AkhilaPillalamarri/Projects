from django.urls import path
from myapp import views
app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='home'),
    path('sample/', views.sample, name='sample'),
    path('our-product/', views.ProductListView.as_view(), name='product-list'),
    path('our-product/<slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('increase-quantity/<pk>/',
         views.IncreaseQuantityView.as_view(), name='increase-quantity'),
    path('decrease-quantity/<pk>/',
         views.DecreaseQuantityView.as_view(), name='decrease-quantity'),
    path('remove-from-cart/<pk>/',
         views.RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/', views.CartView.as_view(), name='summary'),
    
]