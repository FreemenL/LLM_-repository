import socket

# 1.创建socket对象（收发信息）
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.发送连接
client.connect(('127.0.0.1', 9889))

while True:
    # 3.发送消息
    data = input('say:')

    client.send(data.encode('utf-8'))

    if data == '886':
        print('退出...')
        break

    # 4.接收回复
    recv_data = client.recv(1024)
    print(f'收到回复：{recv_data.decode('utf-8')}')

# 5.关闭连接
client.close()