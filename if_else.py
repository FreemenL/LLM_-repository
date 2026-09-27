from random import randint

age = randint(0,100)
if age < 2:
    print(f"{age= },婴儿")
elif age<4:
    print(f"{age= },幼儿")
elif age<=13:
    print(f"{age= },儿童")
elif age<=20:
    print(f"{age= },青少年")
elif age<=65:
    print(f"{age= },成年人")
else:
    print(f"{age= },老年人")