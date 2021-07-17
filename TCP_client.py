import socket

target_host = "0.0.0.0"
target_port = 9996


def rozmowa(wiadomosc):
    #wysyłka danych
    client.send(wiadomosc.encode())
    #odbiór danych
    response = client.recv(4096)
    print(response.decode())

while True:
    # utworzenie obiektu socketa
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # połaczenie z serwerem
    client.connect((target_host, target_port))
    str_2 = input("Podaj co chcesz wysłac na serwer: ")
    rozmowa(str_2)
