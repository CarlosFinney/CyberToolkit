import ssl
import socket
from datetime import datetime

def verificar_ssl(host, porta=443):
    contexto = ssl.create_default_context()

    try:
        with socket.create_connection((host, porta), timeout=5) as sock:
            with contexto.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()

        validade_str = cert['notAfter']
        validade = datetime.strptime(validade_str, '%b %d %H:%M:%S %Y %Z')
        dias_restantes = (validade - datetime.utcnow()).days

        emissor = dict(x[0] for x in cert['issuer']).get('organizationName', 'Desconhecido')

        return {
            "valido": True,
            "emissor": emissor,
            "expira_em": validade.strftime('%d/%m/%Y'),
            "dias_restantes": dias_restantes
        }

    except Exception as e:
        return {"valido": False, "erro": str(e)}