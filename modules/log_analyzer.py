import re
from collections import Counter

PADRAO_FALHA = re.compile(r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)')

def analisar_log(caminho_arquivo, limite_tentativas=3):
    contador_ips = Counter()

    try:
        with open(caminho_arquivo, "r") as f:
            for linha in f:
                match = PADRAO_FALHA.search(linha)
                if match:
                    ip = match.group(1)
                    contador_ips[ip] += 1
    except FileNotFoundError:
        return None

    suspeitos = {ip: qtd for ip, qtd in contador_ips.items() if qtd >= limite_tentativas}

    return {
        "total_falhas": sum(contador_ips.values()),
        "ips_unicos": len(contador_ips),
        "suspeitos": suspeitos
    }