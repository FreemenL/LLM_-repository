import time
import multiprocessing


def work():
    for i in range(10):
        print("工作")
        time.sleep(0.3)


def game():
    for i in range(10):
        print("娱乐")
        time.sleep(0.3)


# work()
# game()


if __name__ == '__main__':
    mutileEleWork = multiprocessing.Process(
        target=work,
        name="niuma"
    )
    mutileEleGame = multiprocessing.Process(
        target=game,
        name="大神"
    )
    mutileEleWork.start()
    mutileEleGame.start()





