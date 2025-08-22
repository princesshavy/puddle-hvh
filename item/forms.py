from django import forms

from .models import Item 

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'price': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        # }