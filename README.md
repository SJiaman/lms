## 简介

一个用Django+MySQL搭建的图书馆管理系统，主要用于练习后端操作数据库与前端交互，用的是MySQL的原生语句。

## 项目环境

+ Python 3.7
+ Django 3.1.1
+ MySQL 5.7
+ Pycharm 2019.2.4

## 修改

```python
# lms/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'PORT': 3306,
        'HOST': 'localhost',
        'NAME': 'lms',  # 改为自己数据库名字
        'USER': 'root',
        'PASSWORD': '123456' # 改为数据库密码
    }
}

```



## 运行方式

确认你的电脑已经正确安装 Python 3.4 以上的版本。

下载项目后，在命令行中进入项目目录，并创建**虚拟环境**：

```bash
python -m venv env
```

运行**虚拟环境**（Windows环境）:

```bash
env\Scripts\activate.bat
```

或（Linux环境）：

```bash
source env/bin/activate
```

自动安装所有依赖项：

```bash
pip install -r requirements.txt
```

最后运行测试服务器：

```bash
python manage.py runserver
```

项目就运行起来了。

![](https://shijin-img.oss-cn-chengdu.aliyuncs.com/blog-img/20200907210148.png)

