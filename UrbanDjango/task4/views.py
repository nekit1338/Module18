from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'platform.html')


def index_2(request):
    return render(request, 'shop.html', {'data': data})


def index_3(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})


data = {
    'games': [
        'Call of Duty: Black Ops 6',
        'Age of Empires 3: Trilogy',
        'Dead by daylight',
        'Dying light 2',
        'Dead island 2'
    ]
}


def add_to_cart(request):
    if request.method == 'POST':
        try:
            game_name = request.POST.get('game')
            if game_name in data['games']:
                cart = request.session.get('cart', {})
                cart[game_name] = cart.get(game_name, 0) + 1
                request.session['cart'] = cart
                return redirect('cart')
            else:
                return HttpResponse("Игра не найдена")
        except (ValueError, TypeError):
            return HttpResponse("Некорректный запрос")
    return HttpResponse("Неверный метод запроса")


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
        request.session.modified = True
    return redirect('cart')
