"""
os模块： 全称叫：Operating System 系统模块 主要是操作文件夹，文件，路径等
    常用函数
        getcwd() 获取当前的工作空间目录(即：你写相对路径时，参考的路径).current work directory: 当前工作目录
        chdir() 改变工作路径. change directory
        rmdir() 删除文件夹，必须是空文件夹。remove directory
        mkdir() 制作文件夹，make directory
        rename() 改名，文件名 或者 文件夹名均可

"""
# 导包
import os

# 演示os 模块的函数
# getcwd() 获取当前的工作空间目录(即：你写相对路径时，参考的路径).current work directory: 当前工作目录
print(os.getcwd())
# chdir() 改变工作路径. change directory
# os.chdir("d:/")
# print(os.getcwd())

# mkdir() 制作文件夹，make directory 如果文件名已存在会报错
# os.mkdir("Isla")

# rmdir() 删除文件夹，必须是空文件夹。remove directory
# os.rmdir("Isla")

# rename() 改名，文件名 或者 文件夹名均可
# os.rename('1.txt', '2.txt')
# os.rename('Isla','Isla_aila')

# listdir() 获取指定目录下 所有的子集文件或者文件夹
file_list = os.listdir('./') # ./ 指当前路径
# file_list = os.listdir('d:/')
print(file_list)