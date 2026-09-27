username = input('请输入用户名')
if username == 'admin':
    password = input('请输入密码')
    if password == '123456':
        print(f"用户名{username}和密码{password}正确，登录成功")
    else:
        print(f"密码{password}错误登录失败")
else:
    print("用户名不存在")