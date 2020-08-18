from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#auth : 로그인/로그아웃 기능이 구현되어 있는 내장 app 즉, 여기서 구현되어 있는 뷰들을 가져온다.


app_name = 'signapp'
#템플릿에서 signapp:path_name 으로 매칭 가능

urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='signapp/signin.html'), name='signin'),
    #loginview는 디폴트로 registration/login.html 이라는 경로의 템플릿 참조하므로 수정해줌
    path('signout/', auth_views.LogoutView.as_view(), name='signout'),
    path('signup/', views.signup, name='signup'),
    #auth app에서도 회원가입을 지원하는 뷰는 제공하지 않음 => 직접 views에다가 뷰를 작성해야 함
    path('mypage/', views.mypage, name='mypage'),


]