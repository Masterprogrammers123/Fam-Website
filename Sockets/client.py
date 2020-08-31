def main():
    import socket

    HEADER = 64
    PORT = 5050
    FORMAT = "utf-8"
    DISCONNECT_MESSAGE = "!EXIT"
    SERVER = "209.226.119.104"
    ADDR = (SERVER, PORT)


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b" " * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
if __name__ == "__main__":
    main()