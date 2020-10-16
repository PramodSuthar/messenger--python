from socket import *
import threading
import sys
from playsound import playsound

FLAG = False


def send_to_server(clsock):
    global FLAG
    while True:
        if FLAG == True:
            break
        send_msg = input('')
        clsock.sendall(send_msg.encode())


def recv_from_server(clsock):
    global FLAG
    while True:
        data = clsock.recv(1024).decode()
        if data =='q':
            print('Closing connection')
            FLAG = True
            break
        print('Server: ' + data)
        playsound('ding.wav')

def main():
    threads = []

    HOST = '192.168.0.191'

    PORT = 8080

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    print('Client is connected to the server! \n')

    t_send = threading.Thread(target=send_to_server, args=(clientSocket,))
    t_rcv = threading.Thread(target=send_to_server, args=(clientSocket))
    threads.append(t_send)
    threads.append(t_rcv)
    t_send.start()
    t_rcv.start()

    t_rcv.join()
    t_send.join()

    print('Exiting')
    sys.exit()

if __name__ == '__main__':
    main()