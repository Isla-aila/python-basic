def info():
    print("----------------")
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生信息")
    print("4.查询单个学生信息")
    print("5.查询所有学生信息")
    print("6.退出系统")

# info()
#2.定义函数student_manager() 实现用户录入什么编号，进行什么操作
def student_manager():
    while True:
        info()

        input_num = input('请输入您要操作的编号：')
        match input_num:
            case '1':
                print("=====添加学生信息=====")
                add_info()
            case '2':
                print("=====删除学生信息=====")
                delete_info()
            case '3':
                print("=====修改学生信息=====")
                update_info()
            case '4':
                print("=====查询单个学生信息=====")
                check_info()
            case '5':
                print("=====查询所有学生信息=====")
                all_student_info()
            case '6':
                print("谢谢使用，正在退出系统")
                break
            case _:
                print("录入有误请重新输入")

# 3.自定义函数add_info 实现：添加学生信息 要求：学号必须唯一
# 格式：学号(id) 姓名(name) 手机号(phone_num)
# 3.1定义列表user_info,用来储存所有学生的信息 格式：列表嵌套字典
user_info = [
    {'id':'001','name':'艾拉','phone_num':'123456'},
    # {'id':'002','name':'水柿司','phone_num':'223456'},
    # {'id':'003','name':'立华奏','phone_num':'323456'},
    # {'id':'004','name':'音无结弦','phone_num':'423456'}
]
# 3.2定义add_info()函数，实现添加学生信息
def add_info():
    # 3.3提示用户录入需要添加的学生学号 ，并接收
    input_id = input('请输入学生学号：')

    # 3.4校验学号是否已存在
    for i in user_info:
        if i['id'] == input_id:
            print('该学号已经被使用，请录入一个全新学号')
            return add_info()
    # 3.5提示用户录入需要添加的学生姓名 ，并接收
    input_name = input('请输入学生姓名：')
    # 3.6提示用户录入需要添加的联系方式 ，并接收
    input_phone_num = input('请输入联系方式：')
    user_info.append({'id':input_id,'name':input_name,'phone_num':input_phone_num})
    print('录入成功，请确认您的信息如下')
    print(f'id:{input_id},name:{input_name},phone_num:{input_phone_num}')

# 4.自定义函数delete_info() 实现：删除学生
def delete_info():
    input_id = input('请输入学生学号：')
    for i in user_info:
        if i['id'] == input_id:
            input_name = input('请输入学生姓名：')
            if i['name'] == input_name:
                #删除信息
                user_info.remove(i)
                print('删除成功')
                break
    else:
        print('您输入的信息有误，请重新输入')
        return

# 5.自定义函数 update_info() 实现修改学生信息，要求：只能修改姓名和手机号
def update_info():
    # 3.3提示用户录入需要修改的学生学号 ，并接收
    input_id = input('请输入学生学号：')
    # 3.4校验学号是否已存在
    for i in user_info:
        if i['id'] == input_id:
    # 3.5学号存在，提示用户确认学生姓名 ，并接收
            boolname = input('是否要修改姓名 y/n')
            if boolname == 'y':
                name_ok = update_name(i)
                if name_ok:
                    print('姓名修改成功')
                    boolphone_num = input('是否要修改手机号 y/n:')
                    if boolphone_num == 'y':
                        new_phone_num = input('请输入新手机号：')
                        i['phone_num'] = new_phone_num
                        print('修改完成，新手机号为', new_phone_num)
                # 无论姓名修改是否成功，都退出循环
                break

            boolphone_num = input('是否要修改手机号 y/n:')
            if boolphone_num == 'y':
                update_phone_num(i)
                break
    else:
        print('学号不存在，请重试')
# 修改姓名
def update_name(i):
    input_name = input('请输入学生原姓名：')
    if i['name'] == input_name:
        new_name = input('请输入学生新姓名：')
        i['name'] = new_name
        print('修改完成，新姓名为', new_name)
        return True
    else:
        print('原姓名输入错误，修改取消')
        return False


# 修改手机号
def update_phone_num(i):
    input_name = input('请输入学生姓名验证信息：')
    if i['name'] == input_name:
        new_phone_num = input('请输入新手机号：')
        i['phone_num'] = new_phone_num
        print('修改完成，新手机号为', new_phone_num)
    else:
        print('姓名验证失败，修改取消')


# 6.自定义函数 check_info() 根据姓名查询单个学生信息
def check_info():
    input_name = input('请输入学生姓名：')
    find_flag = False
    for i in user_info:
        if i['name'] == input_name:
            print(f'id:{i["id"]},name:{i["name"]},phone_num:{i["phone_num"]}')
            find_flag = True
    #        不使用break打断，避免重名学生搜不出来
    if not find_flag:
        print('您输入的姓名不存在')

# 7.查询所有学生信息
def all_student_info():
    # 判断是否有学生信息，如果没有进行提示并结束
    if len(user_info) == 0:
        print('系统内暂无录入数据')
        return

    print("=====全部学生信息=====")
    for stu in user_info:
        print(f'id:{stu["id"]},name:{stu["name"]},phone_num:{stu["phone_num"]}')


if __name__ == '__main__':
    student_manager()