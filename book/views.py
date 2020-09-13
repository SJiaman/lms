from django.shortcuts import render, redirect, reverse
from django.db import connection
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout


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

# def login_in(request):
#     userno = request.POST.get('reader_no')
#     password = request.POST.get('reader_password')
#     # message1 = "所有字段都必须填写！"
#     message2 = "密码错误！"
#     # message3 = "恭喜！登录成功！"
#     # message4 = "用户名不存在！"
#     cursor = connection.cursor()
#     cursor.execute("select reader_password from reader where reader_no='%s'"%userno)
#     reader_password = cursor.fetchone()
#     str_value = str(password)
#
#     # if reader_password:
#     #     return render(request, 'login.html', context={'str_value': str_value})
#     if reader_password == str_value:
#         return redirect(reverse('book:index'))
    # else:
    #     return render(request, 'index.html', context={'message2': message2})
    #     try:
    #         cursor = connection.cursor()
    #         cursor.execute("select book_name,book_type from book where book_name='%s'" % book)
    #         books = cursor.fetchall()
    #         if user.password == password:
    #             return redirect(reverse('book:index'))
    #        else:
    #             message = "密码不正确！"
    #     except:
    #         message = "用户名不存在！"
    #     return render(request, 'login.html', {"message": message})
    # return render(request, ''）


def login(request):
    pass
    return render(request, 'login.html')

def borrow_view(request):
    book_no = request.GET.get('book_no')
    reader_no = 2018001
    cursor = connection.cursor()
    cursor.execute("insert into borrow values ('%s','%s',GETDATE(),GETDATE()+30,GETDATE()+30)"%(book_no,reader_no))
    return redirect(reverse('book:book_list'))

def return_view(request):
    if request.method == 'GET':
        book_no = request.GET.get('book_no')
        cursor = connection.cursor()
        cursor.execute("delete from borrow where book_no='%s'"%book_no)
        return redirect(reverse('book:profile'))


def sign_up(request):
    pass
    return render(request, 'sign-up.html')


def detail(request):
    if request.method == 'GET':
        book = request.GET.get('book_name')
        msg = "抱歉，没有找到书籍"
        cursor = connection.cursor()
        cursor.execute(
            "select book_name,book_type,publisher,author,stock_number,bookstack_no from book where book_name='%s'" % book)
        books = cursor.fetchall()
        if books:
            return render(request, 'search.html', context={'books': books})
        else:
            return render(request, 'search.html', context={'msg': msg})


def book_list(request):
    cursor = connection.cursor()
    cursor.execute("select book_name,book_type,publisher,author,stock_number,bookstack_no,book_no from book")
    books = cursor.fetchall()
    return render(request, 'book-list.html', context={'books': books})


def profile(request):
    cursor = connection.cursor()
    cursor.execute(
        "select book_name,author,borrowed_time,should_returntime,borrow.book_no from book,borrow where book.book_no=borrow.book_no")
    books = cursor.fetchall()
    return render(request, 'profile.html', context={'books': books})

def manage(request):
    cursor = connection.cursor()
    cursor.execute("select book_no,book_name,publisher,author from book")
    books = cursor.fetchall()
    return render(request, 'manage.html', context={'books': books})


def delete(request):
    if request.method == 'POST':
        book_no = request.POST.get('book_no')
        cursor = connection.cursor()
        cursor.execute("delete from book_detail where book_no='%s'" % book_no)
        cursor.execute("delete from book where book_no='%s'" % book_no)
        return redirect(reverse('book:manage'))


def setting(request):
    pass
    return render(request, 'setting.html')
