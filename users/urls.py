from django.conf.urls import url

from . import views
from .views import *

# urlpatterns是被django自动识别的路由列表变量
urlpatterns = [
    # 每个路由信息都需要使用url函数来构造
    # url(路径, 视图)
    # 绝对匹配
    url(r'^index$', views.index, name='试图'),  # r'^index/$', views.index() 不加括号  但是绑定的一定是一个函数
    # 两种关联试图函数的方式 可以全局导入 可以内部导入
    url(r'^say$', say, name='say'),

    url(r'^weather/(\w+)/(\d+)$', weather, name='weather'),  # weather/(\w+)/(\d+)
    url(r'^weather_named/(?P<city>\w+)/(?P<year>\d+)$', weather_named, name='weather_named'),
    # r'^weather_named/(?P<city>\w+)/(?P<year>\d+)$'

    url(r'^query_params$', query_params, name='query_params'),
    url(r'^form$', form, name='form'),
    url(r'^json_data$', json_data, name='json_data'),
    url(r'^header$', header, name='header'),
    url(r'^other$', other, name='other'),
    # 构建响应
    url(r'^create_response$', create_response, name='create_response'),
    # 构建json字符串
    url(r'^create_json$', create_json, name='create_json'),
    # 重定向
    url(r'^redirect_response$', redirect_response, name='redirect_response'),
    # 设置cookie
    url(r'^set_cookie$', set_cookie, name='set_cookie'),
    # 读取cookie
    url(r'^read_cookie$', read_cookie, name='read_cookie'),
    # 设置session值
    url(r'^set_session$', set_session, name='set_session'),
    # 读取session值
    url(r'^read_session$', read_session, name='read_session'),
    # 绑定函数视图
    url(r'^user$', user, name='user'),
    # 绑定类视图
    url(r'^demo_view$', DemoView.as_view()),  # 绑定路由　通过调用as_view()　　方法返回一个视图函数　并且　　as_view（）中又调用dispath　根据请求方式找到对应的方法
    # 模板渲染
    url(r'^render_template$', render_template, name='render_template'),
]
