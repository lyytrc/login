from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from . import models
import hashlib

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method =='GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        context = {
            'message':''
        }
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = models.User.objects.filter(name=username).first()
        if user:
            if password == user.password:
               context['message'] = '登陆成功'
               request.session['is_login'] = True
               request.session['username'] = user.name
               request.session['userid'] = user.id
               return redirect('/index/')
            else:
                context['message'] = '密码不正确'
                return render(request, 'login.html', context=context)
        else:
            context['message'] = '用户未注册'
            return render(request,'login.html', context=context)
def register(request):
    if request.method == 'GET':
        # 注册表单
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user=models.User.objects.filter(email=email).first()
        if user:
            return render(request,'register.html',context={'message':'用户已注册'})
        try:
            user = models.User(name=username, password=password,email=email)
            user.save()
            return render(request,'login.html',context={'message':'注册成功，请继续登陆'})
        except Exception as e:
            print('保存失败',e)
            return redirect('/register')
def logout(request):
    request.session.flush()
    return redirect('/index/')





