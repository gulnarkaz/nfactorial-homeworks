from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('add/', views.add_news, name='add_news'),
    path('102/', views.news_detail_102, name='news_detail_102'), 
    path('<int:pk>/edit/', views.NewsUpdateView.as_view(), name='edit_news'),
]