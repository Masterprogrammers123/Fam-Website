def main_program():
    import socket
    import threading
    # Will change most of the ADDR stuff
    HEADER = 64
    PORT = 5050
    SERVER = socket.gethostname()
    ADDR = (SERVER, PORT)
    FORMAT = "utf-8"
    DISCONNECT_MESSAGE = "!EXIT"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    def handleClient(conn, addr):
        print(f"Yay! {addr} has succeded in the process of connecting!") # Will change this too

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    print(f"{addr} Has Disconnected...")
                    continue
                print(f"[{addr}] {msg}")  # And this
        conn.close()

    def start():
        print()
        server.listen()
        print(f"Server is Listening on {SERVER}.")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handleClient, args=(conn, addr))
            thread.start()
            print(f"ACTIVE CONNECTIONS {threading.activeCount()- 1}")
    start()

if __name__ == "__main__":
    main_program()