import socket
from modules.scanner import scan
from modules.network import get_local_ip
from modules.dns_lookup import consultar_dns
from modules.ssl_check import verificar_ssl
from modules.log_analyzer import analisar_log


def exibir_menu():
    print("\n===== CyberToolkit =====")
    print("1 - Scanner de Portas")
    print("2 - Analisar Logs")
    print("3 - Consulta DNS")
    print("4 - Verificar SSL")
    print("0 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            ip_local = get_local_ip()
            alvo = input(f"\nDigite o IP ou host a escanear (Enter para usar {ip_local}): ").strip()

            if not alvo:
                alvo = ip_local

            try:
                ip = socket.gethostbyname(alvo)
            except socket.gaierror:
                print(f"\nNão foi possível resolver o host '{alvo}'. Tente novamente.")
                continue

            print(f"\nEscaneando {alvo} ({ip})...")

            resultados = scan(ip)

            if resultados:
                print(f"\n{len(resultados)} porta(s) aberta(s) encontrada(s).")
            else:
                print("\nNenhuma porta aberta encontrada nas portas escaneadas (1-100).")

            with open("resultado_scan.txt", "w") as f:
                f.write(f"Alvo: {alvo} ({ip})\n\n")
                for r in resultados:
                    f.write(r + "\n")

            print("Resultado salvo em resultado_scan.txt")

        elif opcao == "2":
            caminho = input("\nDigite o caminho do arquivo de log (ex: auth.log): ").strip()

            resultado = analisar_log(caminho)

            if resultado is None:
                print(f"\nArquivo '{caminho}' não encontrado.")
                continue

            print(f"\nTotal de tentativas falhas: {resultado['total_falhas']}")
            print(f"IPs únicos encontrados: {resultado['ips_unicos']}")

            if resultado["suspeitos"]:
                print("\nIPs suspeitos (3+ tentativas falhas):")
                for ip, qtd in resultado["suspeitos"].items():
                    print(f"  {ip} -> {qtd} tentativas")
            else:
                print("\nNenhum IP suspeito encontrado.")

        elif opcao == "3":
            host = input("\nDigite o domínio para consulta DNS (ex: google.com): ").strip()

            if not host:
                print("Você precisa digitar um domínio.")
                continue

            ip = consultar_dns(host)

            if ip:
                print(f"\n{host} -> {ip}")
            else:
                print(f"\nNão foi possível resolver o domínio '{host}'.")

        elif opcao == "4":
            host = input("\nDigite o domínio para verificar o SSL (ex: google.com): ").strip()

            if not host:
                print("Você precisa digitar um domínio.")
                continue

            resultado = verificar_ssl(host)

            if resultado["valido"]:
                print(f"\nCertificado válido")
                print(f"Emitido por: {resultado['emissor']}")
                print(f"Expira em: {resultado['expira_em']} ({resultado['dias_restantes']} dias restantes)")
            else:
                print(f"\nNão foi possível verificar o SSL: {resultado['erro']}")

        elif opcao == "0":
            print("Encerrando o CyberToolkit...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()