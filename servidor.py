import socket
import threading


print("Aguardando conexão de um cliente")

def novoCliente():
       while True:
              conn, end = s.accept()  #aceitando uma conexão
              threading.Thread(target=conexao, args=(conn,end)).start()

def conexao(conn,end):

       while True:
              print("Conectado em :", end)
              data = conn.recv(2048) #recebendo mensagem do cliente
              msg = data.decode()    #decodificanco mensagem do cliente
              print('Mensagem recebida do cliente: ', msg)
              
              if msg != 'fim':       #mensagem diferente de 'fim' o servidor digita uma resposta ao cliente
                     mensagem = input('Digite uma mensagem: ')
                     conn.send(mensagem.encode())
              else:                  #caso a mensagem seja igual a 'fim' o servidor é encerrado e envia uma mensagem de 'Fim' para o cliente
                     print('Conexão encerrada')
                     conn.send(str.encode('Fim'))
                     conn.close
                     break

if __name__ == '__main__': 
       HOST = 'localhost'
       PORTA = 50000
       s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       s.bind((HOST,PORTA))    #vinculando o socket ao endereço
       s.listen(5)              #habilitando o servidor a receber conexão
       threading.Thread(target=novoCliente, args=()).start()