from django.shortcuts import render,redirect,reverse
from django.db import connection
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# 测试
# def book(request):
#    return HttpResponse("Hello, world!")


def index(request):
    pass
    return render(request, 'index.html')

# def login_view(request):
#     reader_no = request.POST.get('reader_no')
#     reader_password = request.POST.get('reader_password')
#     msg="账号或密码错误"
#     user = authenticate(reader_no=reader_no,reader_password=reader_password)
#     if user is not None:
#         login(request,user)
#         return redirect(reverse('book:index'))
#     else:
#         pass

def login(request):
    pass
    return render(request, 'login.html')

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
    cursor = connection.cursor()
    cursor.execute("select book_no,book_name,publisher,author from book")
    books = cursor.fetchall()
    return render(request, 'manage.html', context={'books': books})

def delete(request):
    if request.method == 'POST':
        book_no = request.POST.get('book_no')
        cursor = connection.cursor()
        cursor.execute("delete from book_detail where book_no='%s'"%book_no)
        cursor.execute("delete from book where book_no='%s'"%book_no)
        return redirect(reverse('book:manage'))

def setting(request):
    pass
    return render(request, 'setting.html')
