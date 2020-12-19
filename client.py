import socket

HEADER = 64
PORT = 5050
SERVER = " "  # local ipv4 from the computer with the server
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def main():
    connected = True
    while connected:
        message = input("Msg: ")
        if message == "@quit":
            connected = False

        send(message)

    send(DISCONNECT_MESSAGE)


if __name__ == "__main__":
    main()
