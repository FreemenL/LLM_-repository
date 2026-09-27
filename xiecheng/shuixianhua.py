def gen_shuixianhua():
    for num in range(100, 1000):
        a = num // 100  # 百位
        b = num // 10 % 10  # 十位
        c = num % 10  # 个位
        if a ** 3 + b ** 3 + c ** 3 == num:
            yield num

if __name__ == '__main__':
    gendef = gen_shuixianhua()
    print(gendef)

    for  i in gendef:
         print(i)