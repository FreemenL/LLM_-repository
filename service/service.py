import socket
import random

# 1.创建socket对象
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 设置端口复用
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 2.绑定操作
# 特殊的ip地址：服务器接收来自任何能连接到这台机器的外部机器
server.bind(('0.0.0.0', 9898))

# 3.等待连接
server.listen(55)
list_back = ['呵呵', '哈哈', '嘿嘿']
# 4.接收连接
# 阻塞方法：一直等待客户端连接
print('服务器已经启动成功，等待连接....')
while True:  # 可以和多个客户端连接（排队）

    try:
        client, addr = server.accept()
        print(f'客户端{addr}接入成功...')

        while True:  # 和当前客户端持续交互，直到退出为止
            # 5.接收客户端消息
            data = client.recv(1024)
            print(f'接收到客户端{addr}，发送的消息：{data.decode('utf-8')}')

            if data == '886':
                print(f'到客户端{addr}，已退出！！！')
                client.close()
                break
            # 6.回复客户端消息
            client.send(list_back[random.randint(0, len(list_back)-1)].encode('utf-8'))
    except Exception as e:
        print(e)
        print('客户端退出....')
