from django import forms

from .models import Product
PUBLISH_CHOICES = (
	('', '-------'),
	('publish', 'Publish'),
	('draft', 'Draft'),
)


class ProductAddForm(forms.Form):

	title = forms.CharField()
	description = forms.CharField(
		widget=forms.Textarea(
			attrs={
				"class": "custom_class",
				"placeholder": "description"
			}
		)
	)
	price = forms.DecimalField()
	publish = forms.ChoiceField(choices=PUBLISH_CHOICES)

	def clean_price(self):
		price = self.cleaned_data.get('price')
		if price < 1:
			raise forms.ValidationError("The list price should be a whole number, no decimals or cents.")
		else:
			return price


class ProductModelForm(forms.ModelForm):
	publish = forms.ChoiceField(choices=PUBLISH_CHOICES)

	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]
		widgets = {
			"description": forms.Textarea(
				attrs={
					"placeholder": "New Description"
				}
			),
			'title': forms.TextInput(
				attrs={
					"placeholder": "Title"
				}
			)
		}

	def clean_price(self):
		price = self.cleaned_data.get('price')
		if price < 1:
			raise forms.ValidationError("The list price should be a whole number, no decimals or cents.")
		else:
			return price

	def clean_title(self):
		title = self.cleaned_data.get('title')
		if len(title) > 3:
			return title
		else:
			raise forms.ValidationError("Title must be grater than 3 characters long.")