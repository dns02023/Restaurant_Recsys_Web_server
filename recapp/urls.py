from django.urls import path
from . import views

app_name = 'recapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:place_id>/', views.place_detail, name='detail'),
    path('review/create/<int:place_id>/', views.review_create, name='review_create'),
    path('review/create/<int:review_id>', views.review_modify, name='review_modify'),
    path('review/delete/<int:review_id>', views.review_delete, name='review_delete'),
]