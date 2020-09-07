from django.urls import path
from . import views

app_name = 'book'

urlpatterns= [
    path('', views.index, name='index'),
    path('search/', views.detail, name='search'),
    path('book-list/', views.book_list, name='book_list'),
    path('login/', views.login, name='login'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile'),
    path('manage/', views.manage, name='manage'),
    path('setting/', views.setting, name='setting'),
]