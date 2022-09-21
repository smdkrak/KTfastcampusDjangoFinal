from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        error_messages={"required": "이메일을 입력해주세요."}, max_length=64, label="이메일"
    )
    username = forms.CharField(
        error_messages={"required": "유저이름을 입력해주세요."},
        label="유저명",
    )
    password1 = forms.CharField(
        error_messages={"required": "비밀번호를 입력해주세요."},
        widget=forms.PasswordInput,
        label="비밀번호",
    )
    password2 = forms.CharField(
        error_messages={"required": "비밀번호를 입력해주세요."},
        widget=forms.PasswordInput,
        label="비밀번호 확인",
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="아이디", error_messages={'required':"아이디를 입력하세요"}, required=True)
    password = forms.CharField(label="비밀번호", error_messages={'required':"비밀번호를 입력하세요"}, widget=forms.PasswordInput, required=True)
    # TODO: 2. login 할 때 form을 활용해주세요 DONE
    print("OK")
