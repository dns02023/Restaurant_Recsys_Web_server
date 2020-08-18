from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

#현재 문제는 장고에서 기본으로 제공되는 회원가입 기능을 쓰는데 이것은 user가 가질 수 있는 속성이 제한되어 있어서
#특수문자를 포함하는 sofo 유저명을 추가할 수 없음 => 새로운 user 객체를 만들 필요가 생김 or Profile 모델을 만들자

#회원가입을 위한 form
class UserForm(UserCreationForm):

    email = forms.EmailField(label="e-mail")
    #sofo_name = forms.CharField(max_length=50, label="sofo_name")

    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('sofo_name',)