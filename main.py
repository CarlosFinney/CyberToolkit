import socket
from modules.scanner import scan
from modules.network import get_local_ip

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
            print("Análise de Logs em desenvolvimento...")

        elif opcao == "3":
            print("Consulta DNS em desenvolvimento...")

        elif opcao == "4":
            print("Verificação SSL em desenvolvimento...")

        elif opcao == "0":
            print("Encerrando o CyberToolkit...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()