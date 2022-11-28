import socket

HOST = 'localhost'
PORTA = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORTA))     #conectando ao servidor

while True:
    mensagem = input('Digite uma mensagem: ')
    s.send(mensagem.encode())       #enviando uma mensagem ao servidor

    data = s.recv(2048)             #recebendo a mensagem do servidor
    msg = data.decode()             #decodificando a mensagem
    print("Mensagem do servidor: ", msg)
    if msg == 'Fim':                #se mensagem for 'Fim' o servidor foi encerrado
        print('Servidor desconectou')
        s.close
        break