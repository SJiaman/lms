from django.shortcuts import render,redirect,reverse
from django.db import connection
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

# 测试
# def book(request):
#    return HttpResponse("Hello, world!")


def index(request):
    pass
    return render(request, 'index.html')

def login(request):
    pass
    return render(request,'login.html')

def sign_up(request):
    pass
    return render(request,'sign-up.html')

def detail(request):
    if request.method == 'GET':
        book = request.GET.get('book_name')
        cursor = connection.cursor()
        cursor.execute("select book_name,book_type,publisher,author,stock_number,bookstack_no from book where book_name='%s'"%book)
        books = cursor.fetchall()
        return render(request, 'search.html', context={'books':books})

def book_list(request):
        cursor = connection.cursor()
        cursor.execute("select book_name,book_type,publisher,author,stock_number,bookstack_no from book")
        books = cursor.fetchall()
        return render(request, 'book-list.html', context={'books': books})

def profile(request):
    pass
    return render(request, 'profile.html')

def manage(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        cursor.execute("insert into(book_no,book_name,book_type,book_type,author,publisher,st')")
        books = cursor.fetchall()
        return render(request, 'manage.html', context={'books': books})

def setting(request):
    pass
    return render(request, 'setting.html')
