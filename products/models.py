from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.


class Product(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=False, blank=True)
	description = models.TextField(null=True)
	price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99)
	sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=15.99, blank=True)

	def __unicode__(self):
		return self.title


def product_presave_receiver(sender, instance, *args, **kwargs):
	if instance.slug != slugify(instance.title):
		instance.slug = slugify(instance.title)


pre_save.connect(product_presave_receiver, sender=Product)


# def product_post_save_reciever(sender, instance, *args, **kwargs):
#
# 	if instance.slug != slugify(instance.title):
# 		instance.slug = slugify(instance.title)
# 		instance.save()
#
#
# post_save.connect(product_post_save_reciever, sender=Product)