"""
pymysql 模块解释
    概述：
        它属于第三方的模块，用之前需要安装一些，它是Python操作MySQL数据库的规范和规则
        里面定义了一些API(函数)，可以帮我们是此案通过Python操作MySQL,进行 增删改查的操作

        安装方式：
        方式1：DOS命令方式：pop install pymysql[-i 镜像地址]
        方式2：导包的时候安装
            写完包名后，按下alt+enter ,给出建议，选择install 包名

    pymysql的操作步骤：
        1.获取连接对象            Python链接MySQL的对象
        2.获取游标对象            可以执行SQL语句的对象
        3.执行SQL语句，获取结果
        4.操作结果集
        5.释放资源
"""
import pymysql