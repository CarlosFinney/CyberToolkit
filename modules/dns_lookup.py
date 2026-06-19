import socket

def consultar_dns(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror:
        return None