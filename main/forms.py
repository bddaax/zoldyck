from django import forms
from .models import Product

class ProductEntryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'service', 'experience', 'rating', 'stock']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 100:
            raise forms.ValidationError('Rating must be between 0 and 100.')
        return rating
