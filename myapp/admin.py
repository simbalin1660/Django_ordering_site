from django.contrib import admin
from myapp.models import Post, NewTable, Order_with_user

# Register your models here.

admin.site.register(Post)
admin.site.register(NewTable)


# Order admin頁面的顯示設定
class OrderAdmin(admin.ModelAdmin):
    # 顯示的欄位
    list_display = ('id', 'order', 'name', 'price', 'date')
    # 可以點選欄位進行排序
    list_filter = ('order',)
    # 可以搜尋的欄位
    search_fields = ('name', 'price', 'order')
    # 欄位排序
    ordering = ('order', 'price')


class OrderwithUserAdmin(admin.ModelAdmin):
    # 顯示的欄位
    list_display = ('id', 'orderer_name', 'name', 'price', 'date')
    # 可以點選欄位進行排序
    list_filter = ('orderer_name',)
    # 可以搜尋的欄位
    search_fields = ('name', 'price', 'orderer_name')
    # 欄位排序
    ordering = ('orderer_name', 'price')


admin.site.register(Order_with_user, OrderwithUserAdmin)
