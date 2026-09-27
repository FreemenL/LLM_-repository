import threading
import time

def music():
    for i in range(10):
        print(f"music{i}")
        time.sleep(0.2)

def coding():
    for i in range(10):
        print(f"coding{i}")
        time.sleep(0.2)

if __name__ == '__main__':
    threading.Thread(target=music).start()
    threading.Thread(target=coding).start()



