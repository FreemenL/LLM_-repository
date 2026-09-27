import time
import multiprocessing
def chatQQ(name):
    for i in range(100):
        print(f"和{name}聊qq")
        time.sleep(0.1)

def chatWX(name):
    for i in range(100):
        print(f"和{name}聊WX")
        time.sleep(0.2)


def chatSoul(name):
    for i in range(100):
        print(f"和{name}聊WX")
        time.sleep(0.3)



# chatQQ()
# chatWX()
# chatSoul()

if __name__ == '__main__':
    multiprocessing.Process(target=chatQQ, name="chatQQ",args=("夏江",)).start()
    multiprocessing.Process(target=chatWX, name="chatWX",args=("芳菲",)).start()
    multiprocessing.Process(target=chatSoul, name="chatSoul",args=("大菲",)).start()

