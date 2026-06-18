import socket
from concurrent.futures import ThreadPoolExecutor

SERVICOS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    21: "FTP",
    25: "SMTP",
    3306: "MySQL",
    53: "DNS"
}

resultados = []


def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))

        if result == 0:
            servico = SERVICOS.get(port, "Desconhecido")
            texto = f"Porta {port} ABERTA ({servico})"
            print(texto)
            resultados.append(texto)

        sock.close()

    except:
        pass


def scan(ip, inicio=1, fim=100, threads=50):
    global resultados
    resultados = []

    print(f"\nEscaneando {ip}...\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in range(inicio, fim + 1):
            executor.submit(scan_port, ip, port)

    return resultados