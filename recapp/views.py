from django.shortcuts import render, get_object_or_404, redirect
from .models import Place, Review
from django.utils import timezone
from .forms import ReviewForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django_recsys.settings import get_secret
import requests
import logging

logger = logging.getLogger(__name__)

RECSYS_RESTAPI = get_secret("RECSYS_RESTAPI")

# Create your views here.
def index(request):


    #홈화면에 바로 맛집 목록을 띄워 준다.
    page = request.GET.get('page', '1')
    #디폴트 페이지는 첫번째 페이지로 지정
    place_list = Place.objects.order_by('id')
    #이름 순으로 정렬

    paginator = Paginator(place_list, 20)
    page_obj = paginator.get_page(page)

    recommends = list()
    if request.user.is_authenticated:
        target = request.user
        # 개인화 추천 (CF) 요청 => 추천 API 서버 => 추천 결과 => res
        res = ((requests.post(RECSYS_RESTAPI + '/recommender/cfrecommend',
                              data={"sofo_name": target.profile.sofo_name}))).json()
        if res != 'No Review':
            for i in range(len(res)):
                temp = get_object_or_404(Place, pk=res[i])
                recommends.append(temp)

    context = {'place_list' : page_obj, 'recommends' : recommends}
    #place_list를 20개씩 쪼깬 page 객체를 render 함수에 변수(place_list)로 넘겨줌
    return render(request, 'recapp/place_list.html', context)

def place_detail(request, place_id):
    place = get_object_or_404(Place ,pk=place_id)
    # 사용자 행동(맛집 조회) 로그 수집
    if request.user.is_authenticated:
        logger.info('{} {} [{}]'.format(request.user.username, 'BROWSE' ,place.place_name))
    # 유사한 맛집 (CB) 추천 요청 => 추천 API 서버 => 추천 결과 => res
    res = ((requests.post(RECSYS_RESTAPI + '/recommender/cbrecommend', data={"id" : place.id}))).json()
    similars = list()
    for i in range(len(res)):
        temp = get_object_or_404(Place, pk=res[i])
        similars.append(temp)
    context = {'place' : place, 'similars' : similars}
    return render(request, 'recapp/place_detail.html', context)

#리뷰는 로그인이 필요하므로 로그아웃 상태에서 리뷰생성을 호출하면 바로 로그인 화면으로 이동되게
#login_required를 붙여줌
@login_required(login_url='signapp:signin')
def review_create(request, place_id):

    place = get_object_or_404(Place, pk=place_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        #리뷰 등록 시도(POST), 사용자가 폼 형식으로 작성한 폼 객체를 받는다.
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            #현재 로그인한, 즉 현재 요청을 보내는 user 객체를 author로 설정
            review.place = place
            #review의 foreign key인 place와 관계 형성
            review.save()
            #폼 형식으로 리뷰 등록하고 redirect로 return

            # training 데이터로 수집
            requests.post(RECSYS_RESTAPI + '/etl/reviewetl',
                          data={"user_name": review.author.profile.sofo_name, "place_name" : review.place.place_name, "rating" : review.rating})

            return redirect('recapp:detail', place_id=place.id)

    else:
        form = ReviewForm()
    #리뷰 등록 이전에 폼을 가져오는 것
    context = {'place': place, 'form': form}
    #place_detail.html에 넘겨줄 인자들 정의, 'place', 'form'
    return render(request, 'recapp/place_detail.html', context)

@login_required(login_url='signapp:signin')
def review_modify(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.author:
        messages.error(request, '이 리뷰를 수정할 권한이 없습니다.')
        return redirect('recapp:detail', place_id = review.place.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.modify_date = timezone.now()
            review.save()
            return redirect('recapp:detail', place_id = review.place.id)
        #폼이 invalid 이면 어차피 html에서 form_error를 띄워준다.
    else:
        form = ReviewForm(instance=review)
        #GET이면 그냥 폼 형식만 생성해서 띄워주기
    context = {'review' : review, 'form' : form}
    return render(request, 'recapp/review_form.html', context)
    #review를 수정하기 위한 별도 수정 템플릿으로 보내기

@login_required(login_url='signapp:signin')
def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.author:
        messages.error(request, '이 리뷰를 삭제할 권한이 없습니다.')
    else:
        review.delete()
    return redirect('recapp:detail', place_id = review.place.id)








