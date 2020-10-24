from django.http import HttpResponse
from django.shortcuts import render, redirect

users = {'yaozihan': '123', 'yuanjia': '1234', 'shuaixiangyu': '12345'}
gender = {'yaozihan': '男', 'yuanjia': '男', 'shuaixiangyu': '女'}
# for item in users:
#     list1 = list(item)


def bcd(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def my_print(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username1 = request.POST.get('username1')
        password1 = request.POST.get('password1')
        if username1 in users.keys():
            if users[username1] == password1:
                return HttpResponse('成功登陆！')
            elif password1 != users[username1]:
                error = {'error': '错误'}
                return render(request, 'login.html', error)
        elif username1 not in users.keys():
            error1 = {'error1': '用户不存在，请注册新用户'}
            return redirect('yzh:regi')


def abc(request):
    if request.method == 'POST':
        username2 = request.POST.get('username2')
        password2 = request.POST.get('password2')
        sex = request.POST.get('sex')
        if username2 in users.keys():
            error2 = {'error': '用户名已存在，请重新注册'}
            return render(request, 'register.html', error2)
        elif username2 not in users.keys() and username2.isalnum():
            if len(username2) <= 10:
                users.update({username2: password2})
                gender.update({username2: sex})
                rp1 = {'rp1': '注册成功，请登陆！'}

                return render(request, 'login.html', rp1)
            elif len(username2) > 10:
                rp2 = {'rp2': '用户名过长，请重新注册！'}
                return render(request, 'register.html', rp2)
        elif username2 not in users.keys() and not username2.isalnum():
            error3 = {'error3': '用户名包含非法符号，请重新注册'}
            return render(request, 'register.html', error3)
    else:
        return render(request, 'register.html')
