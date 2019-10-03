from socket import *

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


port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print("{}번 포트로 접속 대기 중...".format(port))

connectionSock, addr = serverSock.accept()
print(str(addr), "에서 접속이 확인되었습니다.")

while 1:
    sendData = input(">>> ")
    connectionSock.send(sendData.encode('utf-8'))

    recvData = connectionSock.recv(1024)
    print("상대방: ", recvData.decode('utf-8'))
