from socket import *
from threading import *
import time

# 1
# serverSock = socket(AF_INET, SOCK_STREAM)
# serverSock.bind(('', 8080))
# serverSock.listen(1)
#
# connectionSock, addr = serverSock.accept()
# print(str(addr),'에서 접속이 확인되었습니다.')
#
# data = connectionSock.recv(1024)
# print('받은 데이터 : ', data.decode('utf-8'))
#
# connectionSock.send('I am a server.'.encode('utf-8'))
# print('메시지를 보냈습니다.')

# 2
# port = 8080
#
# serverSock = socket(AF_INET, SOCK_STREAM)
# serverSock.bind(('', port))
# serverSock.listen(1)
#
# print("{}번 포트로 접속 대기 중...".format(port))
#
# connectionSock, addr = serverSock.accept()
# print(str(addr), "에서 접속이 확인되었습니다.")
#
# while 1:
#     sendData = input(">>> ")
#     connectionSock.send(sendData.encode('utf-8'))
#
#     recvData = connectionSock.recv(1024)
#     print("상대방: ", recvData.decode('utf-8'))

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
# serverSock = socket(AF_INET, SOCK_STREAM)
# serverSock.bind(('', port))
# serverSock.listen(1)
#
# print("{}번 포트로 접속 대기 중...".format(port))
#
# connectionSock, addr = serverSock.accept()
# print(str(addr), "에서 접속이 확인되었습니다.")
#
# while 1:
#     send(connectionSock)
#     receive(connectionSock)

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

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print("{}번 포트로 접속 대기 중...".format(port))

connectionSock, addr = serverSock.accept()
print(str(addr), "에서 접속이 확인되었습니다.")

sender = Thread(target=send, args=(connectionSock,))
receiver = Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while 1:
    time.sleep(1)
    pass
