from django import forms
from .models import Order_with_user


# model建立的表單格子、字體大小、字體樣式等修改須從form著手

class OrderModelForm(forms.ModelForm):
    class Meta:
        # 指定資料庫
        model = Order_with_user
        # 顯示的欄位
        fields = '__all__'

        # 表單
        widgets = {
            # size:表格寬度
            # title:滑鼠移動到表格上時的提示文字
            'name': forms.TextInput(attrs={'class': 'form-control', 'title': '請輸入餐點名稱', 'size': 20}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'title': '請輸入價格', 'size': 20}),
        }

        # 顯示的字預設是欄位名
        labels = {
            'name': '餐點',
            'price': '價格',
            'orderer_name': '訂餐者',
        }
