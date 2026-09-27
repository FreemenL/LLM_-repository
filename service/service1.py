import socket
import random
import multiprocessing


def chat_client(client, addr):
    try:
        while True:  # 和当前客户端持续交互，直到退出为止
            # 5.接收客户端消息
            data = client.recv(1024)
            print(f'接收到客户端{addr}，发送的消息：{data.decode('utf-8')}')

            if data.decode("utf-8") == '886':
                print(f'到客户端{addr}，已退出！！！')
                client.close()
                break
            list_back = ['呵呵', '哈哈', '嘿嘿']
            # 6.回复客户端消息
            client.send(list_back[random.randint(0, len(list_back) - 1)].encode('utf-8'))
    finally:
        client.close()
        print(f"客户端{addr}聊天结束")

if __name__ == '__main__':
    # 1.创建socket对象
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 设置端口复用
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2.绑定操作
    # 特殊的ip地址：服务器接收来自任何能连接到这台机器的外部机器
    server.bind(('0.0.0.0', 9889))

    # 3.等待连接
    server.listen(100)

    # 4.接收连接
    # 阻塞方法：一直等待客户端连接
    print('服务器已经启动成功，等待连接....')
    try:
        while True:  # 可以和多个客户端连接（排队）
            client, addr = server.accept()
            print(f'客户端{addr}接入成功...,为其分配专属自进程进行聊天')
            chat_process= multiprocessing.Process(target=chat_client, args=(client, addr))
            chat_process.daemon=True
            chat_process.start()
            client.close()
    finally:
        server.close()


