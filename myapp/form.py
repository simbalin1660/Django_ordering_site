from django import forms
from .models import Order_with_user


# model建立的表單格子、字體大小、字體樣式等修改須從form著手

class OrderModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['orderer_name'] = forms.CharField(widget=forms.HiddenInput(), initial=user)
            self.fields['orderer_name'].disabled = True

    class Meta:
        model = Order_with_user
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'title': '請輸入餐點名稱', 'size': 20}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'title': '請輸入價格', 'size': 20}),
        }
        labels = {
            'name': '餐點',
            'price': '價格',
            'orderer_name': '訂餐者',
        }
        exclude = ('orderer_name',)


class OrderForm(forms.Form):
    orderer_name = forms.CharField( max_length=255, required=False, widget=forms.HiddenInput())
    orderer_name.disabled
    name = forms.CharField( max_length=255)
    price = forms.IntegerField()


    class Meta:
        model = Order_with_user
        fields = ['orderer_name', 'name', 'price']
        labels = {
            'name': '餐點',
            'price': '價格',
            'orderer_name': '訂餐者',
        }
