import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"Porta {port}: ABERTA")
        else:
            print(f"Porta {port}: FECHADA")

        sock.close()

    except Exception as e:
        print(f"Erro ao escanear porta {port}: {e}")