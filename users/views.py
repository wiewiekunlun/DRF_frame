import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.core.urlresolvers import reverse  # 注意导包路径
from django.template import loader
from django.utils.decorators import method_decorator
from django.views import View


def index(request):  # 视图函数的第一个传入参数必须定义，用于接收Django构造的包含了请求数据的HttpReqeust对象
    '''
    index 视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    '''

    return HttpResponse('hello the world')
    # 视图函数的返回值必须为  HttpResponse  响应对象


def say(request):  # 接收HttpReqeust对象
    '''
    reverse 反解析
    :return:
    '''
    # 查询index路由名称对应的路径
    # 没有添加namespace
    # url = reverse('user:试图')
    # 添加namespace之后
    url = reverse('user:say')
    print(url)

    return HttpResponse('say')


# request.args 查询字符串数据 /users/index?a=1&b=2&a=3&c=4

# request.form 表单数据 请求体数据
# request.json json数据 请求体数据
# request.files 文件 请求体数据
# request.data 纯文本 请求体数据

# request.headers 请求头数据

# users/1
# app.route('users/<id>',...)
# 路径中的信息
# weather/beijing/2018 表示获取北京2018年天气情况
# weather/shandong/2017 表示获取山东2017年天气情况

def weather(request, city, year):
    # weather(,city,year)
    # 使用分组时,有几个分组就会向函数中传递几个参数
    # 而且传递的顺序与分组顺序一致
    print('city: ', city)
    print('year: ', year)

    return HttpResponse('OK')


def weather_named(request, year, city):
    # weather_named(,city=city,year=year)
    # 参数顺序不再重要
    print('city: ', city)
    print('year: ', year)

    return HttpResponse('OK')


# 获取查询字符串数据
def query_params(request):
    # request.GET 包含查询字符串数据, 返回的是QueryDict对象(同一个键带有多个值的情况)
    data = request.GET
    print(data)  # 键值对的形式返回字典
    print(type(data))  # <class 'django.http.request.QueryDict'>
    print(data.get('a'))  # 默认获取最后一个值
    print(data.get('b'))  #
    print(data.getlist('a'))  # 获取同一个键下的所有的值
    return HttpResponse('OK')


# 获取form表单数据    表单类型的请求体数据
def form(request):
    # request.POST包含表单数据 返回的是QueryDict对象--处理同一个键带有多个值的情况
    data = request.POST
    print(data)
    # 打印单个数据
    print(data.get('a'))
    print(data.get('b'))
    # 打印同一个建下的所有值
    print(data.getlist('a'))

    data = request.GET
    print(data)

    return HttpResponse('OK')


# 非表单类型的请求体数据
def json_data(request):
    # 1 拿到原始数据 request.body    bates
    # 2 转换为字符串
    # 3 使用json.loads(bady_str) 转换为python内置对象
    body_bates = request.body
    bady_str = body_bates.decode()  # 默认utf-8
    data = json.loads(bady_str)
    print(data)
    return HttpResponse('OK')


# 请求头
def header(request):
    # request.META 包含请求头数据   request.META为字典类型。
    headers = request.META
    print(headers['CONTENT_LENGTH'])  # 26
    print(headers['CONTENT_TYPE'])  # application/json
    return HttpResponse('OK')


# 请求对象的其他属性
def other(request):
    print('method:', request.method)
    print('user:', request.user)
    # print('method:', request.url)
    print('encoding:', request.encoding)
    print('FILES:', request.FILES)
    return HttpResponse('OK')


# 构建响应  两种构建 HttpResponse 响应对象的方式
def create_response(request):
    # 构建相应对象    1 使用django.http.HttpResponse来构造响应对象。
    response = HttpResponse(content='创建响应', content_type='text/plain', status='201')

    # 2 通过HttpResponse对象属性来设置响应体、响应体数据类型、状态码
    # response = HttpResponse('itcast python')
    # response.status_code = 410
    response['Itcast'] = 'Python'
    return response


# 构建json字符串    自动创建相应对象的方式
def create_json(request):
    # data = {
    #     "a": 10,
    #     "b": 20
    # }
    data_list = [1, 2, 3]
    # 手动构建json响应
    # json_str = json.dumps(data)
    # response = HttpResponse(content=json_str, content_type='application/json')

    # 使用JsonResponse构建json响应
    # response = JsonResponse(data)
    # 如果返回列表数据 那么要添加safe=False  默认的是字典 django 认为不安全数据
    response = JsonResponse(data_list, safe=False)
    return response


# 重定向
def redirect_response(request):
    # 重定向使用完整路径
    return redirect('/users/index')


# 设置cookie
def set_cookie(request):
    # 创建httpresponse对象
    response = HttpResponse('OK')
    # 通过HttpResponse对象中的set_cookie方法来设置cookie
    response.set_cookie('python', 'Django', max_age=3600)
    return response


# 读取cookie
def read_cookie(request):
    # 通过HttpRequest对象的COOKIES属性来读取本次请求携带的cookie值。
    # request.COOKIES为字典类型
    cookie1 = request.COOKIES.get('python')
    print(cookie1)
    return HttpResponse('OK')


# 设置session值
def set_session(request):
    # 拿到客户对应的session字典
    session = request.session

    session['test'] = 'test'  # 存入redis数据库

    session['test1'] = 'value1'

    session.set_expiry(100)  # 10 秒过期

    return HttpResponse('OK')


# 读取session值  删除键值对
def read_session(request):
    # 拿到客户对应的session字典
    session = request.session

    cookie1 = request.COOKIES.get('test')  # None  session 的值不是存储在cookie中的
    print(cookie1)

    session_value = session.get('test1', 'none')  # value1
    print(session_value)

    # del session['test1']  # 删除指定的某个键值

    session.flush()  # 删除的是整个字段

    session.clear()  # 删除值部分

    return HttpResponse('OK')


# method path version : GET /users/index HTTP/1.1
# GET,POST,PUT,DELETE
#
# GET: 查询数据
# POST: 创建数据
# PUT: 更新数据
# DELETE: 删除数据

# 定义函数试图
def user(request):
    # 操作user数据库表
    method = request.method

    if method == 'GET':
        # 查询用户信息
        return HttpResponse('get')

    elif method == 'PUT':
        # 更新用户信息
        return HttpResponse('put')

    elif method == 'POST':
        # 更新用户信息
        return HttpResponse('post')

    elif method == 'DELETE':
        # 更新用户信息
        return HttpResponse('delete')

    else:
        return HttpResponse('未知的请求方法')


# 自定义装饰装饰器
def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用')
        print('请求路径%s'%request.path)
        return func(request, *args, **kwargs)  # 返回一个视图函数
    return wrapper


# 定义商品类  和user方式一样　重复　　类的继承
# @my_decorator
def goods(request):
    pass

my_decorator(goods)  # 装饰器装饰函数类似于传参, 所以也可以这样装饰

# 定义类视图   类视图可以将视图对应的不同请求方式以类中的不同方法来区别定义
@method_decorator(my_decorator, name='dispatch')
class DemoView(View):           # 注意：定义类视图继承的是    View
    """类视图：处理注册"""

    # @method_decorator(my_decorator)  加了method_decorator, 才可以即在函数上进行装饰，　又可以在类函数上进行装饰，　原因是被装饰函数的参数不一致，　所以只用　my_decorator　会导致出现装饰不一致的情况
    def get(self, request):
        """处理GET请求，返回注册页面"""
        return HttpResponse('get')

    def post(self, request):
        """处理POST请求，实现注册逻辑"""
        return HttpResponse('post')

    def put(self, request):
        return HttpResponse('put')

    def delete(self, request):
        return HttpResponse('delete')

# # 怎么将请求格式和对应的方法联系起来
# def dispatch(self, request, *args, **kwargs):
#     # Try to dispatch to the right method; if a method doesn't exist,
#     # defer to the error handler. Also defer to the error handler if the
#     # request method isn't on the approved list.
#     # http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
#     # GET 是否在http_method_names中,
#     if request.method.lower() in self.http_method_names:
#         # 如果在　返回属性 get attribule(self, get)－－＞ def get(self, request):
#         # 在这里将请求格式和对应的视图函数联系起来
#         handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
#
#     else:
#         handler = self.http_method_not_allowed
#         # get(request)--> HttpResponse('get')  返回相应对象
#     return handler(request, *args, **kwargs)

class CreateMixin(object):
    def create(self):
        # 执行创建数据操作
        return HttpResponse('创建成功')


class UpdateMixin(object):
    def update(self):
        # 执行更新数据操作
        return HttpResponse('更新成功')


class ListMixin(object):
    def list(self):
        # 执行查询数据操作
        return HttpResponse('查询成功')


class DeleteMixin(object):
    def drop(self):
        # 执行删除数据操作
        return HttpResponse('删除成功')


class DemoView2(ListMixin, DeleteMixin, View):
    def get(self, request):
        return self.list()

    def delete(self, request):
        return self.drop()  # 方法名称一样就是重写方法了


class DemoView3(ListMixin, CreateMixin, View):
    def get(self, request):
        return self.list()

    def post(self, request):
        return self.create()


# 模板渲染
def render_template(request):
    # 方法１　

    # # 1 获取模板　　返回模板对象
    # template = loader.get_template('index.html')
    #
    # # 构建上下文
    # context = {'city':'北京'}
    #
    #
    # # 2 渲染模板　
    # return HttpResponse(template.render(context))

    # 方法２
    # render(request对象, 模板文件路径, 模板数据字典)

    context = {
        'city': '北京',
        'adict': {
            'name': '西游记',
            'author': '吴承恩'
        },
        'alist': [1, 2, 3, 4, 5]
    }
    # 第一个request必须传递,第二个模板名字,第三个上下文
    return render(request, 'index.html', context)









