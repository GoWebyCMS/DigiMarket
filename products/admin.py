from django.contrib import admin

# Register your models here.

from .models import Product


class ProductAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'description', 'price', 'sale_price', 'slug')
	search_fields = ['title', 'description']
	list_filter = ['price']
	list_editable = ['sale_price']
	# prepopulated_fields = {"slug": ('title',)}
	# class Meta:
	# 	model = Product

admin.site.register(Product, ProductAdmin)