from modules.scanner import scan_port
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
            ip = get_local_ip()

            print(f"\nIP detectado automaticamente: {ip}")

            for port in range(1, 101):
                scan_port(ip, port)

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