from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login


def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username = data['login'], password = data['password'])
        if user is not None:
            login(request, user)
            request.session['is_auth'] = user.username
            return render(request, 'main.html')
        else:
            return render(request, 'auth/auth.html', {'error': 'wrong login or password.'})
    else:
        return render(request, 'auth/auth.html')

   
def reg(request):
    if request.method == "POST":
        not_valid = ''
        data = request.POST     
        if (User.objects.filter(username = data['login'])):
            not_valid = 'Такой login уже есть'
            return render(request, 'reg.html',  {'not_valid_regist': not_valid})
        
        user = User.objects.create_user(data['login'],data['email'],data['password'])
        user.first_name = data['name']
        if data['password'] == data['password2']:
            user.save()
            auth(request)
            return render(request, "main.html")
        
        else:
            not_valid = 'Неверный пароль'
            return render(request, 'reg.html',  {'not_valid_regist': not_valid})
        
    else:
        return render(request, 'auth/reg.html')
    
def out(request):
    logout(request)
    return render(request, "main.html")