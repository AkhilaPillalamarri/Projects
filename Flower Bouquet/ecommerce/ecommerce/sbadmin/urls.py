
from django.urls import path
from sbadmin import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product/list', views.product_home, name='project_list'),
    path('product/create', views.product_create, name='product_create'),
    path('product/edit/<int:pk>', views.product_update, name='product_update'),
    path('product/delete/<int:pk>', views.product_delete, name='product_delete'),
    ###################Address########
    path('address/list', views.address_home, name='address_list'),
    path('address/create', views.address_create, name='address_create'),
    path('address/edit/<int:pk>', views.address_update, name='address_update'),
    path('address/delete/<int:pk>', views.address_delete, name='address_delete'),
    ###################Category########
    path('category/list', views.category_home, name='category_list'),
    path('category/create', views.category_create, name='category_create'),
    path('category/edit/<int:pk>', views.category_update, name='category_update'),
    path('category/delete/<int:pk>', views.category_delete, name='category_delete'),
    ###################Colour########
    path('colour/list', views.colour_home, name='colour_list'),
    path('colour/create', views.colour_create, name='colour_create'),
    path('colour/edit/<int:pk>', views.colour_update, name='colour_update'),
    path('colour/delete/<int:pk>', views.colour_delete, name='colour_delete'),
    ###################Size########
    path('size/list', views.size_home, name='size_list'),
    path('size/create', views.size_create, name='size_create'),
    path('size/edit/<int:pk>', views.size_update, name='size_update'),
    path('size/delete/<int:pk>', views.size_delete, name='size_delete'),

    ###################OrderItem########
    path('orderitem/list', views.orderitem_home, name='orderitem_list'),
    path('orderitem/create', views.orderitem_create, name='orderitem_create'),
    path('orderitem/edit/<int:pk>', views.orderitem_update, name='orderitem_update'),
    path('orderitem/delete/<int:pk>', views.orderitem_delete, name='orderitem_delete'),
    ###################Order########
    path('order/list', views.order_home, name='order_list'),
    path('order/create', views.order_create, name='order_create'),
    path('order/edit/<int:pk>', views.order_update, name='order_update'),
    path('order/delete/<int:pk>', views.order_delete, name='order_delete'),
    
    ###################Coustomer########
    path('customer/list', views.customer_home, name='coustomer_list'),
    path('customer/create', views.customer_create, name='coustomer_create'),
    path('customer/edit/<int:pk>', views.customer_update, name='coustomer_update'),
    path('customer/delete/<int:pk>', views.customer_delete, name='coustomer_delete'),
]

