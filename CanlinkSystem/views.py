from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


# 登陆界面
def login(request):
    if request.method == "GET":  # 这里是要大写的
        return render(request, "login.html")
    if request.method == "POST":
        userID = request.POST.get("userID", None)
        password = request.POST.get("password", None)
        print(userID, password)
        if userID == 'admin' and password == '123456':
            return render(request, 'index.html')
        else:
            return HttpResponse("ERROR！登录失败，请联系网站管理员！")


# 机车百科
def CRHTrain(request):
    return render(request, 'baike/CRHtrain.html')


# 地图管理
def maplist(request):
    return render(request, 'baike/maps/CRHmpas.html')
