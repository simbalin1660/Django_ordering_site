import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product
from django.http import Http404
from django.template.loader import get_template
import random
from .form import ExpenseModelForm
from .models import Expense

food_counter = 0

def about(request):
    template = get_template('footer.html')
    quotes = ['早晚都要做，不如現在開始做',
              '放學回家社關心你']
    quote = random.choice(quotes)
    return render(request, 'footer.html', locals())

def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())

def disp_detail(request, Type):
    try:
        p = Product.objects.get(Type=Type)
    except Product.DoesNotExist:
        raise Http404('找不到指定的產品訂單')
    return render(request, 'disp_detail.html', locals())

def homepage(request):

    restaurant_list = ['麥當勞', '肯德基', 'subway', '陸家', '回家吃', '佳臻便當', '八方',
                       '火車站雞肉飯', '麻婆丼丼', '大內', '海饌',
                       '土庫肉燥飯', '臻愛', '第一讚炒飯', '福氣來水餃', '陳家麵館', '咱兜灶腳', '阿Bin炒飯專賣',
                       '冠味賞鴨肉飯楠梓店', '矮仔魯爌肉飯', '滿溢食堂', '好味越南料理',
                       '郜記涼麵', '香宴蛋包飯', '小林雞肉飯', '後街鴨肉羹', '橋川(火車站麻婆)', '吉大福漢堡']
    restaurant = random.choice(restaurant_list)

    quotes = ['早晚都要做，不如現在開始做，放學回家社關心你']
    quote = random.choice(quotes)

    return render(request, 'home/index.html', locals())


def order(request):

    expenses = Expense.objects.all()

    form = ExpenseModelForm

    if request.method == 'POST':
        form = ExpenseModelForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'order/index.html', locals())

def newrestaurant(request):
    return render(request, 'newrestaurant.html', locals())

def position(request):
    return render(request, 'position.html', locals())

def login(request):
    template = get_template('login/index.html')
    try:
        userid = request.GET['user_id']
        userpass = request.GET['user_pass']
    except:
        userid = None

    if userid != None and userpass == '123':
        verifeid = True
    else:
        verifeid = False

    return render(request, 'login/index.html', locals())