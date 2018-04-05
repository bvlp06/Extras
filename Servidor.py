import socket
import codecs
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msg= ''

s.bind((HOST,PORT)) # servidor em escuta, ativação
s.listen(1)# maximo number de conexões

while True :
    c,e=s.accept()# conexão e endereço cliente
    print('Conectado com ',e)
    while True:#segundo laço para mais mensagens
        msg= input('Qual a mensagem a ser enviada?')
        c.send(str(msg).encode())#enviando a mensagem
    #c.close()
    


