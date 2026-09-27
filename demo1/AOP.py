

def connect_decorator(func):
    def wrapper(*args, **kwargs):
        print("打开数据库连接")
        print(kwargs)
        result = func(*args, **kwargs)
        print("关闭数据库连接")
        return result
    return wrapper


@connect_decorator
def create(a,b,c):
    print('执行数据库增加操作')

@connect_decorator
def delete(a,b,c):
    print("执行数据库删除操作")

@connect_decorator
def update(a,b,c):
    print("执行数据库更新操作")

@connect_decorator
def find(a,b,c):
    print("执行数据库查找操作")



create(1,2,c=2)
delete(1,2,c=2)
update(1,2,c=2)
find(1,2,c=2)

