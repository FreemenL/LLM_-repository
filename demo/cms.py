from customer import Customer


class CMS:
    def __init__(self):
        self.cus_dict = {}

    def display_menu(self):
        print(""""
            **********************客户管理系统***************************
            1.添加客户
            2.删除客户
            3.修改客户
            4.查询客户
            5.显示客户
            6.退出
        """)
    def add_cus_cid(self):
        c_id = 'None'
        for i in range(3):
            if i<2:
                c_id = input("请输入客户id\n")
                if Customer.check_id(c_id):
                    break
                else:
                    print("id 必须为纯数字")
            else:
                c_id = input("最后一次机会了请输入客户id\n")
                if Customer.check_id(c_id):
                    break
                else:
                    print("终止添加客户id")
                    return False

        if c_id in self.cus_dict:
            print("id 已经存在不能重复添加")
            return False
        else:
            return c_id

    def add_cus_name(self):
        cus_name = 'None'
        for i in range(3):
            if i < 2:
                cus_name = input("请输入客户名字\n")
                if Customer.check_name(cus_name):
                    break
                else:
                    print("客户名字必须为字母或中文")
            else:
                cus_name = input("最后一次机会了请输入客户名字\n")
                if Customer.check_id(cus_name):
                    break
                else:
                    print("终止添加客户名字")
                    return False
        return cus_name

    def add_cus_age(self):
        cus_age = input('请输入年龄')
        if Customer.check_age(cus_age):
            return cus_age
        else:
            print("年龄暂时不添加也行")
            return "None"

    def add_cus_phone(self):
        cus_phone = input('请输入手机号')

        if Customer.check_phone(cus_phone):
            return cus_phone
        else:
            print("手机号暂时不添加也行")
            return "None"

    def add_cus_email(self):
        cus_email = input('请输入邮箱')

        if Customer.check_email(cus_email):
            return cus_email
        else:
            print("邮箱暂时不添加也行")
            return "None"

    def add_cus(self):
        if not(cus_id := self.add_cus_cid()):
            return
        if not(cus_name := self.add_cus_name()):
            return

        cus_age = self.add_cus_age()
        cus_phone = self.add_cus_phone()
        cus_email = self.add_cus_email()

        cus = Customer(cus_id, cus_name, cus_age, cus_phone, cus_email)
        self.cus_dict[cus_id] = cus
        print("添加成功")


    def start(self):
        try:
            while True:
                self.display_menu()
                choice = int(input("请输入选项"))
                match choice:
                    case 1:
                        self.add_cus()
                    case 2:
                        print("执行删除操作")
                    case 3:
                        print("执行修改操作")
                    case 4:
                        print("执行查寻操作")
                    case 5:
                        print("执行显示操作")
                    case 6:
                        print("退出")
                    case _:
                        print("输入错误请重新输入")
        except (EOFError,KeyboardInterrupt):
                print("输入错误请重新输入")

if __name__ == "__main__":
    cms = CMS()
    cms.start()