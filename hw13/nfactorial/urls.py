from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('<int:first>/add/<int:second>/', views.add, name='add'),
    path('transform/<str:text>/', views.upper, name='upper'),
    path('check/<str:word>/', views.palindrome, name='palindrome'),
    path('calc/<int:first>/<str:operation>/<int:second>/', views.calculator, name='calculator'),
]