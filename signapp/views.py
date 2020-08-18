from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from signapp.forms import UserForm, ProfileForm
from signapp.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

# 회원가입 : 리뷰생성 뷰와 비슷한 맥락임 post인지 get인지를 판단한다.
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile = profile_form.save(commit=False)

            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)

            profile.user = user
            # 로그인 전까지는 anonymous user 객체이므로 user 객체를 매핑 할 수 없어서
            # authenticate, login 과정을 거친 후 user 객체가 로그인되면 프로필에 매핑
            profile.save()
            return redirect('index')

    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'signapp/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required(login_url='signapp:signin')
def mypage(request):
    user = request.user
    context = {'user' : user}
    return render(request, 'signapp/mypage.html', context)


# def signup(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#
#             user_form.save()
#             profile = profile_form.save(commit=False)
#
#             username = user_form.cleaned_data.get('username')
#             raw_password = user_form.cleaned_data.get('password1')
#
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#
#             profile.user = user
#             # 로그인 전까지는 anonymous user 객체이므로 user 객체를 매핑 할 수 없어서
#             # authenticate, login 과정을 거친 후 user 객체가 로그인되면 프로필에 매핑
#             profile.save()
#
#         else:
#             if profile_form.is_valid() == False:
#                 error_msg = '회원 가입에 실패했습니다\n{}'.format(
#                     '\n'.join(
#                         [f'- {error}'
#                          for key, value in profile_form.errors.items()
#                          for error in value]))
#                 return HttpResponse(error_msg)
#                 #return redirect('signapp:signup')
#
#         return redirect('index')
#
#     else:
#         user_form = UserForm()
#         profile_form = ProfileForm()
#     return render(request, 'signapp/signup.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })







