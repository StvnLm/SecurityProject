import socket, sys

global host
global port
global sock

# Create the socket
def create_socket():
    try:
        global host
        global port
        global sock
        host = ""
        port = 5678
        sock = socket.socket()
    except socket.error as se:
        print("Socket creation error" + str(se))


# Bind socket to port and wait for connection from client
def bind_socket():
    try:
        global host
        global port
        global sock
        print("Binding socket to port: " + str(port))
        sock.bind((host, port))
        sock.listen(5)
    except socket.error as se:
        print("Socket binding error" + str(se))


# Establish connection with client
def establish_connection():
    conn, address = sock.accept()
    print(address)
    print(f"Connecting has been established for {str(address[0])}:{str(address[1])}")
    send_commands(conn)
    conn.close()


def send_commands(conn):
    # print(conn)
    while True:
        cmd = input()
        if cmd.upper() == "QUIT":
            conn.close()
            sock.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            c_resp = str(conn.recv(1024), "utf-8")
            print(c_resp)



if __name__ == '__main__':
    create_socket()
    bind_socket()
    establish_connection()

