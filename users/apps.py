from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'  # 表示这个配置类是加载到哪个应用的
    # 子应用的名字

    verbose_name = '用户管理'  # 设置该应用的直观可读的名字 此名字在Django提供的Admin管理站点中会显示