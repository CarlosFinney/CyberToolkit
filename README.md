# CyberToolkit

Ferramenta de linha de comando para tarefas básicas de segurança de rede, feita em Python. Projeto pessoal para praticar conceitos de scanning, redes e automação enquanto estudo para certificação CCNA e área de SOC/NOC.

## Funcionalidades

- **Scanner de Portas**: escaneia um IP ou domínio informado pelo usuário, verificando portas comuns (1-100) e identificando serviços conhecidos (SSH, HTTP, HTTPS, FTP, SMTP, MySQL, DNS). Usa multithreading para acelerar o scan.
- **Análise de Logs**: em desenvolvimento.
- **Consulta DNS**: em desenvolvimento.
- **Verificação SSL**: em desenvolvimento.

## Como usar

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/seu-usuario/CyberToolkit.git
cd CyberToolkit
```

Execute:

```bash
python main.py
```

Escolha a opção 1 no menu e informe o IP ou host que deseja escanear (ou pressione Enter para usar seu próprio IP local).

### Exemplo de uso

```
Digite o IP ou host a escanear (Enter para usar 172.16.0.2): scanme.nmap.org
Escaneando scanme.nmap.org (45.33.32.156)...
Porta 22 ABERTA (SSH)
Porta 80 ABERTA (HTTP)
2 porta(s) aberta(s) encontrada(s).
Resultado salvo em resultado_scan.txt
```

O host `scanme.nmap.org` é mantido publicamente pelo projeto Nmap para testes de scanner, sem necessidade de autorização.

## Estrutura do projeto

```
CyberToolkit/
├── main.py
├── modules/
│   ├── scanner.py
│   └── network.py
├── resultado_scan.txt
└── README.md
```

## Tecnologias

- Python 3
- Bibliotecas padrão: `socket`, `threading`, `concurrent.futures`

## Aviso

Use este scanner apenas em hosts que você tem autorização para testar. Escanear redes ou IPs de terceiros sem permissão pode ser ilegal.

## Próximos passos

- Implementar análise de logs (detecção de tentativas de login suspeitas)
- Implementar consulta DNS
- Implementar verificação de validade de certificado SSL
- Permitir configurar a faixa de portas pelo usuário
