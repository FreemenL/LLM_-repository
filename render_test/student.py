student_list = [
    {"name": "王五", "age": 31, "bonus": 100},
    {"name": "赵六", "age": 41, "bonus": 100},
    {"name": "刘八", "age": 51, "bonus": 100},
    {"name": "张三", "age": 12, "bonus": 100},
    {"name": "李四", "age": 21, "bonus": 100},
]

sortFun = lambda stu: stu["age"]


student_list.sort(key=sortFun,reverse=True)

print(student_list)

mylist = [1,2,4,5,56,6,7,7,8]
func  = lambda x:x*2

res = map(func,mylist)

print(list(res))

