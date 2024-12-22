from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['ivan', 'petr', 'anton']


def index(request):
    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return HttpResponse(f'Приветствуем, {username}!')
        else:
            info['form'] = form
    else:
        info['form'] = UserRegister()
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if len(username) > 30:
            errors.append('Имя пользователя не должно превышать 30 символов')
        if username in users:
            errors.append('Пользователь уже существует')
        if password != repeat_password:
            errors.append('Пароли не совпадают')
        if not age.isdigit() or int(age) < 18:
            errors.append('Вам меньше 18 лет')
        if len(age) > 3:
            errors.append('Возраст не может содержать более 3 цифр')
        if int(age) > 120:
            errors.append('Возраст не может быть больше 120')
        if len(password) < 8:
            errors.append('Пароль должен быть не менее 8 символов')
        if errors:
            info['errors'] = errors
            info['username'] = username
            info['password'] = password
            info['repeat_password'] = repeat_password
            info['age'] = age
        else:
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'registration_page.html', {'info': info})
