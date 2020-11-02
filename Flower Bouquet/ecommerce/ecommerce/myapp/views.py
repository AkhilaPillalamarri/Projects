from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import *
from .forms import *
from .utils import get_or_set_order_session
# Create your views here.
def index(request):
	return render(request, 'myapp/index.html')

def sample(request):
    return render(request, 'myapp/sample.html')

class ProductListView(generic.ListView):
    template_name = 'myapp/Product.html'

    def get_queryset(self):
        qs = Product.objects.all()
        category = self.request.GET.get('category', None)
        if category:
            qs = qs.filter(Q(primary_category__name=category) |
                           Q(secondary_categories__name=category)).distinct()
        return qs

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context.update({
            "categories": Category.objects.values("name")
        })
        return context


class ProductDetailView(generic.FormView):
    template_name = 'myapp/product_detail.html'
    form_class = AddToCartForm

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs["slug"])

    def get_success_url(self):
        return reverse("myapp:summary")

    def get_form_kwargs(self):
        kwargs = super(ProductDetailView, self).get_form_kwargs()
        kwargs["product_id"] = self.get_object().id
        return kwargs

    def form_valid(self, form):
        order = get_or_set_order_session(self.request)

        product = self.get_object()

        item_filter = order.items.filter(
            product=product,
            colour=form.cleaned_data['colour'],
            size=form.cleaned_data['size'],
        )

        if item_filter.exists():
            item = item_filter.first()
            item.quantity += int(form.cleaned_data['quantity'])
            item.save()

        else:
            new_item = form.save(commit=False)
            new_item.product = product
            new_item.order = order
            new_item.save()

        return super(ProductDetailView, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(**kwargs)
    #     context['product'] = self.get_object()
    #     return context

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context.update({
            "product": self.get_object(),
            "product1": Product.objects.all().order_by('-id')[:4],
            "product2": Product.objects.all().order_by('-id')[4:8],
            "product3": Product.objects.all().order_by('-id')[8:12],
        })
        return context


class CartView(generic.TemplateView):
    template_name = "myapp/cart.html"

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context["order"] = get_or_set_order_session(self.request)
        return context


class IncreaseQuantityView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.quantity += 1
        order_item.save()
        return redirect("myapp:summary")


class DecreaseQuantityView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        if order_item.quantity <= 1:
            order_item.delete()
        else:
            order_item.quantity -= 1
            order_item.save()
        return redirect("myapp:summary")


class RemoveFromCartView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.delete()
        return redirect("myapp:summary")