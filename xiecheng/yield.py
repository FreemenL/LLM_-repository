# yield 用在函数中用于返回生成器对象


def mygen():
    print("11111")
    yield 1
    print("2222")
    yield "2"
    print("3333")

if __name__ == '__main__':

    my_gen = mygen()
    print(my_gen)

    print(next(my_gen))
    print(next(my_gen))
