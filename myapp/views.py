from django.shortcuts import render, redirect
from django.template.loader import get_template
from .form import OrderModelForm
from .models import Order_with_user
import random


def homepage(request):
    restaurant_list = ['麥當勞', '肯德基', 'subway', '陸家', '回家吃', '佳臻便當', '八方',
                       '火車站雞肉飯', '麻婆丼丼', '大內', '海饌',
                       '土庫肉燥飯', '臻愛', '第一讚炒飯', '福氣來水餃', '陳家麵館', '咱兜灶腳', '阿Bin炒飯專賣',
                       '冠味賞鴨肉飯楠梓店', '矮仔魯爌肉飯', '滿溢食堂', '好味越南料理',
                       '郜記涼麵', '香宴蛋包飯', '小林雞肉飯', '後街鴨肉羹', '橋川(火車站麻婆)', '吉大福漢堡']
    restaurant = random.choice(restaurant_list)

    # 儲存使用者選擇的餐廳
    ctx = {}
    # 判斷是否為POST請求
    if request.POST:
        ctx['rlt'] = request.POST[restaurant]

    return render(request, 'home/index.html', locals())


def order_list(request):
    print(request.user.username)
    orders = Order_with_user.objects.all()
    form = OrderModelForm()

    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():  # is_valid()判斷表單是否通過驗證
            form.save()
            return redirect("/order")

    context = {
        'orderer': request.user.username,
        'orders': orders,
        'form': form
    }

    return render(request, 'order/index.html', context)


# def ordermod(request, pk):
#     orderdata = Order_with_user.objects.get(id=pk)
#     if request.method == 'POST':
#         orderer = request.POST.get('order')
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#     try:
#
#         return render(request, 'order/index.html', locals())
#     except:
#         message = '資料讀取錯誤'
#     return render(request, 'order/index.html', locals())


# def orderdel(request):
#     if order != None:
#         if request.method == 'POST':
#             order = request.POST['order']
#         try:
#             expense = order.objects.get(order=order).delete()
#             return render(request, 'order/index.html', locals())
#         except:
#             message = '資料讀取錯誤'
#         return render(request, 'order/index.html', locals())


def newrestaurant(request):
    return render(request, 'newrestaurant.html', locals())


def position(request):
    return render(request, 'position.html', locals())


def login(request):
    template = get_template('login/index.html')
    try:
        userid = request.GET['user_id']
        userpass = request.GET['user_pass']
    except KeyError:
        userid = None

    if userid != None and userpass == '123':
        verifeid = True
    else:
        verifeid = False

    return render(request, 'login/index.html', locals())
