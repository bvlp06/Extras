import socket
import time
import codecs
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

HOST=input('Insira o IP de destino')
print('Conectando')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('\nVocê está conectado á :',HOST)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    while True:#laço para mais mensagens
        dados=s.recv(1024)
        print('Mensagem Recebida: ', dados.decode())
