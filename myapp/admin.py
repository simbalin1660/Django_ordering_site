from django.contrib import admin
from myapp.models import Post, NewTable, Product, Expense

# Register your models here.

admin.site.register(Post)
admin.site.register(NewTable)
admin.site.register(Product)
admin.site.register(Expense)