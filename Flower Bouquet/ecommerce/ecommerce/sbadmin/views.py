from myapp.models import *
from sbadmin.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'sb-admin/index.html')


@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('/sb-admin/product/list')
                messages.success(request, 'Product has been create.')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, 'sb-admin/product/create.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        
        form = ProductForm(
            request.POST, request.FILES or None, instance=product)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Product has been update.')
                return redirect('/sb-admin/product/list')
            except:
                pass
    else:
        form = ProductForm( instance=product)
    return render(request, 'sb-admin/product/update.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Course Deleted Successfully.')
        return redirect('/sb-admin/product/list')
    return render(request, 'sb-admin/product/delete.html', {'object': product})


@user_passes_test(lambda u: u.is_superuser)
def product_home(request):
    product = Product.objects.all().order_by('-id')
    context = {'product': product}

    return render(request, 'sb-admin/product/list.html', context)

###########Address##############################


@user_passes_test(lambda u: u.is_superuser)
def address_create(request):
    if request.method == "POST":
        form = AddressForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('/sb-admin/address/list')
                messages.success(request, 'Address has been create.')
            except:
                pass
    else:
        form = AddressForm()
    return render(request, 'sb-admin/address/create.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def address_update(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == "POST":
        
        form = AddressForm(
            request.POST, request.FILES or None, instance=address)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Address has been update.')
                return redirect('/sb-admin/address/list')
            except:
                pass
    else:
        form = AddressForm(instance=address)
    return render(request, 'sb-admin/address/update.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def address_delete(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == 'POST':
        address.delete()
        messages.success(request, 'Address Deleted Successfully.')
        return redirect('/sb-admin/address/list')
    return render(request, 'sb-admin/address/delete.html', {'object': address})


@user_passes_test(lambda u: u.is_superuser)
def address_home(request):

    address = Address.objects.all().order_by('-id')
    context = {'product': address}

    return render(request, 'sb-admin/address/list.html', context)


###################CategoryForm##################

@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('/sb-admin/category/list')
                messages.success(request, 'Category has been create.')
            except:
                pass
    else:
        form = CategoryForm()
    return render(request, 'sb-admin/category/create.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        
        form = CategoryForm(
            request.POST, request.FILES or None, instance=category)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Category has been update.')
                return redirect('/sb-admin/category/list')
            except:
                pass
    else:
        form = CategoryForm(instance=category)
    return render(request, 'sb-admin/category/update.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category Deleted Successfully.')
        return redirect('/sb-admin/category/list')
    return render(request, 'sb-admin/category/delete.html', {'object': category})


@user_passes_test(lambda u: u.is_superuser)
def category_home(request):

    category = Category.objects.all().order_by('-id')
    context = {'product': category}

    return render(request, 'sb-admin/category/list.html', context)

###################ColourVariationForm##################


@user_passes_test(lambda u: u.is_superuser)
def colour_create(request):
    if request.method == "POST":
        form = ColourVariationForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('/sb-admin/colour/list')
                messages.success(request, 'ColourVariation has been create.')
            except:
                pass
    else:
        form = ColourVariationForm()
    return render(request, 'sb-admin/colour/create.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def colour_update(request, pk):
    colour = get_object_or_404(ColourVariation, pk=pk)
    if request.method == "POST":
        form = ColourVariationForm(
            request.POST, request.FILES or None, instance=colour)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'ColourVariation has been update.')
                return redirect('/sb-admin/colour/list')
            except:
                pass
    else:
        form = ColourVariationForm(instance=colour)
    return render(request, 'sb-admin/colour/update.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def colour_delete(request, pk):
    colour = get_object_or_404(ColourVariation, pk=pk)
    if request.method == 'POST':
        colour.delete()
        messages.success(request, 'ColourVariation Deleted Successfully.')
        return redirect('/sb-admin/colour/list')
    return render(request, 'sb-admin/colour/delete.html', {'object': colour})


@user_passes_test(lambda u: u.is_superuser)
def colour_home(request):

    colour = ColourVariation.objects.all().order_by('-id')
    context = {'product': colour}

    return render(request, 'sb-admin/colour/list.html', context)

###################SizeVariationForm##################


@user_passes_test(lambda u: u.is_superuser)
def size_create(request):
    if request.method == "POST":
        form = SizeVariationForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('/sb-admin/size/list')
                messages.success(request, 'SizeVariation has been create.')
            except:
                pass
    else:
        form = SizeVariationForm()
    return render(request, 'sb-admin/size/create.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def size_update(request, pk):
    size = get_object_or_404(SizeVariation, pk=pk)
    if request.method == "POST":
        
        form = SizeVariationForm(
            request.POST, request.FILES or None, instance=size)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'SizeVariation has been update.')
                return redirect('/sb-admin/size/list')
            except:
                pass
    else:
        form = SizeVariationForm(instance=size)
    return render(request, 'sb-admin/size/update.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def size_delete(request, pk):
    size = get_object_or_404(SizeVariation, pk=pk)
    if request.method == 'POST':
        size.delete()
        messages.success(request, 'SizeVariation Deleted Successfully.')
        return redirect('/sb-admin/size/list')
    return render(request, 'sb-admin/size/delete.html', {'object': size})


@user_passes_test(lambda u: u.is_superuser)
def size_home(request):

    size = SizeVariation.objects.all().order_by('-id')
    context = {'product': size}

    return render(request, 'sb-admin/size/list.html', context)

###################OrderItemForm##################


@user_passes_test(lambda u: u.is_superuser)
def orderitem_create(request):
    if request.method == "POST":
        form = OrderItemForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('/sb-admin/orderitem/list')
                messages.success(request, 'OrderItem has been create.')
            except:
                pass
    else:
        form = OrderItemForm()
    return render(request, 'sb-admin/orderitem/create.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def orderitem_update(request, pk):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    if request.method == "POST":
        
        form = OrderItemForm(
            request.POST, request.FILES or None, instance=orderitem)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'orderitem has been update.')
                return redirect('/sb-admin/orderitem/list')
            except:
                pass
    else:
        form = OrderItemForm(instance=orderitem)
    return render(request, 'sb-admin/orderitem/update.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def orderitem_delete(request, pk):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'POST':
        orderitem.delete()
        messages.success(request, 'OrderItem Deleted Successfully.')
        return redirect('/sb-admin/orderitem/list')
    return render(request, 'sb-admin/orderitem/delete.html', {'object': orderitem})


@user_passes_test(lambda u: u.is_superuser)
def orderitem_home(request):

    orderitem = OrderItem.objects.all().order_by('-id')
    context = {'product': orderitem}

    return render(request, 'sb-admin/orderitem/list.html', context)

###################Order##################


@user_passes_test(lambda u: u.is_superuser)
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('/sb-admin/order/list')
                messages.success(request, 'Order has been create.')
            except:
                pass
    else:
        form = OrderForm()
    return render(request, 'sb-admin/order/create.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        
        form = OrderForm(request.POST, request.FILES or None, instance=order)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'order has been update.')
                return redirect('/sb-admin/order/list')
            except:
                pass
    else:
        form = OrderForm(instance=order)
    return render(request, 'sb-admin/order/update.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order Deleted Successfully.')
        return redirect('/sb-admin/order/list')
    return render(request, 'sb-admin/order/delete.html', {'object': order})


@user_passes_test(lambda u: u.is_superuser)
def order_home(request):

    order = Order.objects.all().order_by('-id')
    context = {'product': order}

    return render(request, 'sb-admin/order/list.html', context)

###################Payment##################





@user_passes_test(lambda u: u.is_superuser)
def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('/sb-admin/customer/list')
                messages.success(request, 'Payment has been create.')
            except:
                pass
    else:
        form = CustomerForm()
    return render(request, 'sb-admin/customer/create.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def customer_update(request, pk):
    customer = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        
        form = CustomerForm(
            request.POST, request.FILES or None, instance=customer)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'customer has been update.')
                return redirect('/sb-admin/customer/list')
            except:
                pass
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'sb-admin/customer/update.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def customer_delete(request, pk):
    customer = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer Deleted Successfully.')
        return redirect('/sb-admin/customer/list')
    return render(request, 'sb-admin/customer/delete.html', {'object': customer})


@user_passes_test(lambda u: u.is_superuser)
def customer_home(request):

    customer = User.objects.all().order_by('-id')
    context = {'product': customer}

    return render(request, 'sb-admin/customer/list.html', context)
