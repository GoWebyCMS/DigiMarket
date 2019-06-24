from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


# Create your views here.
from .models import Product
from .forms import ProductModelForm


def product_edit(request, slug=None, template_path='products/product_add_edit.html'):
	product = get_object_or_404(Product, slug=slug)
	form = ProductModelForm(request.POST or None, instance=product)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	# response
	context = dict(form=form, submit_btn="Edit Product")
	return render(request, template_path, context)


def product_create(request, template_path='products/product_add_edit.html'):
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

	context = dict(form=form, submit_btn="Add Product")
	return render(request, template_path, context)


class ProductDetailView(DetailView):
	model = Product

	def get_object(self, *args, **kwargs):
		slug = self.kwargs.get('slug')
		if slug:
			obj = get_object_or_404(Product, slug=slug)
		else:
			obj = super(ProductDetailView, self).get_object(*args, **kwargs)
		return obj


class ProductListView(ListView):
	model = Product

	def get_queryset(self, *args, **kwargs):
		qs = super(ProductListView, self).get_queryset(**kwargs)
		# qs = filter()
		for item in qs:
			print (item)
		return qs