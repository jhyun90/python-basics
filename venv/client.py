from socket import *
from threading import *
import time

# 1
# clientSock = socket(AF_INET, SOCK_STREAM)
# clientSock.connect(('127.0.0.1', 8080))
# print('연결 확인 됐습니다.')
#
# clientSock.send('I am a client'.encode('utf-8'))
# print('메시지를 전송했습니다.')
#
# data = clientSock.recv(1024)
# print('받은 데이터 : ', data.decode('utf-8'))

# 2
# port = 8080
#
# clientSock = socket(AF_INET, SOCK_STREAM)
# clientSock.connect(('127.0.0.1', port))
# print('접속 완료')
#
# while 1:
#     recvData = clientSock.recv(1024)
#     print("상대방: ", recvData.decode('utf-8'))
#
#     sendData = input(">>> ")
#     clientSock.send(sendData.encode('utf-8'))

# 3
# def send(sock):
#     sendData = input(">>> ")
#     sock.send(sendData.encode('utf-8'))
#
# def receive(sock):
#     recvData = sock.recv(1024)
#     print("상대방: ", recvData.decode('utf-8'))
#
#
# port = 8080
#
# clientSock = socket(AF_INET, SOCK_STREAM)
# clientSock.connect(('127.0.0.1', port))
# print("접속 완료")
#
# while 1:
#     receive(clientSock)
#     send(clientSock)

# 4
def send(sock):
    while 1:
        sendData = input(">>> ")
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while 1:
        recvData = sock.recv(1024)
        print("상대방: ", recvData.decode('utf-8'))


port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))
print("접속 완료")

sender = Thread(target=send, args=(clientSock,))
receiver = Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while 1:
    time.sleep(1)
    pass
