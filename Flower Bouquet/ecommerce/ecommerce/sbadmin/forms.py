from myapp.models import *
from django.forms import ModelForm

class ProductForm(ModelForm):
	class Meta:
	    model = Product
	    fields = '__all__'

class AddressForm(ModelForm):
	class Meta:
	    model = Address
	    fields = '__all__'

class CategoryForm(ModelForm):
	class Meta:
	    model = Category
	    fields = '__all__'

class ColourVariationForm(ModelForm):
	class Meta:
	    model = ColourVariation
	    fields = '__all__'

class SizeVariationForm(ModelForm):
	class Meta:
	    model = SizeVariation
	    fields = '__all__'


class OrderItemForm(ModelForm):
	class Meta:
	    model = OrderItem
	    fields = '__all__'

class OrderForm(ModelForm):
	class Meta:
	    model = Order
	    fields = '__all__'



class CustomerForm(ModelForm):
	class Meta:
	    model = User
	    fields = '__all__'