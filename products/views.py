from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product
from .forms import ProductModelForm


def create_view(request, template_path='products/product_create.html'):
	form = ProductModelForm(request.POST)
	if form.is_valid():
		# get form data
		data = form.cleaned_data
		# save data in db
		new_product = Product()
		new_product.title = data.get('title')
		new_product.description = data.get('description')
		new_product.price = data.get('price')
		new_product.save()

	context = {
		"form": form,
	}
	return render(request, template_path, context)


def detail_view(request, slug=None, template_path='products/detail_view.html'):
	# get item
	product = get_object_or_404(Product, slug=slug)
	context = {'product': product}
	return render(request, template_path, context)


def list_view(request, template_path='products/list_view.html'):
	context = {}
	return render(request, template_path, context)