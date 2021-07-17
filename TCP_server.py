import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9996

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("[*] Nasłuchiwanie na porcie: "+str(bind_ip)+str(bind_port))

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Odebrano: " + str(request.decode()))

    ack_str = "Odebrałem, dzięki!"
    client_socket.send(ack_str.encode())
    client_socket.close()

while True:
    client,addr = server.accept()
    print("[*] Przyjęto połączenie od: " + str(addr))

    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
