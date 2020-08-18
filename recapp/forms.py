from django import forms
from recapp.models import Place, Review

#리뷰생성을 위한 폼
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        #create_time은 자동 생성
        labels = {
            'rating': '평점',
            'content': '한줄평',

        }