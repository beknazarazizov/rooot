from django import forms



class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    descriptions = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    reting=forms.FloatField()
    discount=forms.IntegerField()
    quantity=forms.IntegerField()


# class ProductModelForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         exclude =()