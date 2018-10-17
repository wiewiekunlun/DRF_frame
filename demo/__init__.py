# 如果使用pymysql作为jdango工程的数据库连接驱动, 必须执行以下函数
# 调用manage.py 文件时会自动执行此处的代码
from pymysql import install_as_MySQLdb

install_as_MySQLdb()
# 作用是让Django的ORM能以mysqldb的方式来调用PyMySQL




