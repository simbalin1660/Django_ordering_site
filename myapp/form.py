from django import forms
from .models import Expense

class ExpenseModelForm(forms.ModelForm):


    class Meta:
        model = Expense
        fields = '__all__'
        # 表單
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
        # 標籤
        labels = {
            'name': '餐點',
            'price': '價格'
        }