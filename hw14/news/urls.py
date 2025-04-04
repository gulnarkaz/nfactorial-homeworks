from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('add/', views.add_news, name='add_news'),
    path('102/', views.news_detail_102, name='news_detail_102'), 
    path('<int:pk>/edit/', views.NewsUpdateView.as_view(), name='edit_news'),
    path('sign-up/', views.SignUpView.as_view(), name='signup'),
    path('delete/<int:pk>/', views.DeleteNewsView.as_view(), name='delete_news'),
    path('delete_comment/<int:pk>/', views.DeleteCommentView.as_view(), name='delete_comment'),
    
    # API URLs
    path('api/news/', views.NewsListAPIView.as_view(), name='news_list_api'),
    path('api/news/add/', views.news_add_api, name='news_add_api'),
    path('api/news/<int:pk>/', views.NewsDetailAPIView.as_view(), name='news_detail_api'),
    path('api/news/delete/<int:pk>/', views.NewsDeleteAPIView.as_view(), name='news_delete_api'),
]