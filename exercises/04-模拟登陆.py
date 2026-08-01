#需求：模拟登录，只给3次机会
# 1.假设初始的账号或者密码，并接收
username = 'Aila'
password = 'Isla'
# 2.给3次机会提交账号或者密码
for i in range(3):
# 3.提示用户录入账号或者密码并接收
    input_username = input('请输入账户名：')
    input_password = input('请输入密码：')
# 4.就判断是否录入成功，成功就提示账号登陆成功，结束循环
    if input_username == username and input_password == password:
        print('登陆成功')
        break
# 5.失败就提示错误并提示剩余录入的次数
    else:
        print('输入错误',f'剩余机会{2-i}次' if i < 2 else '输入次数到达上限，账号已被锁定，请于...联系')
