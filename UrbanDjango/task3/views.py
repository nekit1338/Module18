from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'platform.html')


def index_2(request):
    return render(request, 'shop.html', {'data': data})


def index_3(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})


data = {'Call of Duty: Black Ops 6': 'https://www.callofduty.com/ru/blackops6',
        'Age of Empires 3: Trilogy': 'https://store.steampowered.com/app/933110/Age_of_Empires_III_Definitive_Edition',
        'Dead by daylight': 'https://deadbydaylight.com',
        'Dying light 2': 'https://dyinglightgame.com',
        'Dead island 2': 'https://deadisland.com'}


def add_to_cart(request):
    if request.method == 'POST':
        selected_key = request.POST.get('key')
        if selected_key in data:
            cart = request.session.get('cart', {})
            cart[selected_key] = cart.get(selected_key, 0) + 1
            request.session['cart'] = cart
            return redirect('cart')
        else:
            return HttpResponse("Ключ не найден")
    return HttpResponse("Неверный метод запроса")