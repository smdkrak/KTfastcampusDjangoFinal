import re
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password


from .forms import LoginForm, RegisterForm

User = get_user_model()


def index(request):
    return render(request, "index.html")

# def redirect_test(request):
#     print("REDIRECT")
#     return redirect("index")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")
    else:
        logout(request)
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # 그냥 get 쓸 수 X
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # if User.DoesNotExist:
            #     pass
            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                print("유저가 없습니다")
                pass
            else:
                #forms.py 활용
                if user.check_password(password):  
                    login(request,user)
                    # request.session['user'] = form.user_id
                    request.session['user'] = username
                    return HttpResponseRedirect('/')
            # TODO: 1. /login로 접근하면 로그인 페이지를 통해 로그인이 되게 해주세요DONE
            # TODO: 2. login 할 때 form을 활용해주세요DONE
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    # TODO: 3. /logout url을 입력하면 로그아웃 후 / 경로로 이동시켜주세요			DONE			
    return HttpResponseRedirect("/")

# TODO: 8. user 목록은 로그인 유저만 접근 가능하게 해주세요 DONE
# @csrf_exempt
@login_required(login_url="/login")
def user_list_view(request):
    # if request.method == "POST":
    page = int(request.GET.get("pageNum",1))
    userList = User.objects.all()
    users = Paginator(userList,30).get_page(page)
    # TODO: 7. /users 에 user 목록을 출력해주세요DONE
    # TODO: 9. user 목록은 pagination이 되게 해주세요DONE
    return render(request, "users.html", {"users": users})
