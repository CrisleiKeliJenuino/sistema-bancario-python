import os  # Importa a biblioteca para lidar com arquivos

# Variáveis globais
saldo = 0  # Armazena o saldo da conta
limite = 500  # Define o valor máximo permitido por saque
extrato = []  # Lista para armazenar o histórico de transações
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Número máximo de saques permitidos por dia
ARQUIVO_SALDO = "saldo.txt"  # Nome do arquivo onde o saldo será salvo

def carregar_saldo():
    """Carrega o saldo do arquivo, se ele existir."""
    global saldo
    if os.path.exists(ARQUIVO_SALDO):  # Verifica se o arquivo existe
        with open(ARQUIVO_SALDO, "r") as arquivo:
            saldo = float(arquivo.read())  # Lê o saldo do arquivo e converte para float

def salvar_saldo():
    """Salva o saldo atual no arquivo."""
    with open(ARQUIVO_SALDO, "w") as arquivo:
        arquivo.write(str(saldo))  # Escreve o saldo no arquivo

def exibir_menu():
    """Exibe o menu de opções e retorna a opção escolhida pelo usuário."""
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu).lower().strip()  # Converte a entrada para minúsculas e remove espaços extras

def depositar():
    """Permite ao usuário fazer um depósito na conta."""
    global saldo  # Indica que a variável saldo será modificada
    valor = float(input("Informe o valor do depósito: "))  # Solicita o valor do depósito

    if valor > 0:  # Verifica se o valor é válido (positivo)
        saldo += valor  # Adiciona o valor ao saldo
        extrato.append(f"Depósito: R$ {valor:.2f}")  # Registra o depósito no extrato
        salvar_saldo()  # Salva o novo saldo no arquivo
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")  # Mensagem de sucesso
    else:
        print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro para valores negativos ou zero

def sacar():
    """Permite ao usuário sacar um valor da conta, respeitando regras de saldo e limite."""
    global saldo, numero_saques  # Indica que as variáveis serão modificadas
    valor = float(input("Informe o valor do saque: "))  # Solicita o valor do saque

    # Verificações de restrições para saque
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")  # Impede saques negativos ou zero
        return

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")  # Impede saque maior que o saldo disponível
        return

    if valor > limite:
        print("Operação falhou! O valor do saque excede o limite permitido.")  # Impede saque maior que o limite definido
        return

    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")  # Impede saques além do limite diário
        return

    # Se todas as condições forem atendidas, realiza o saque
    saldo -= valor  # Subtrai o valor do saldo
    extrato.append(f"Saque: R$ {valor:.2f}")  # Registra o saque no extrato
    numero_saques += 1  # Incrementa o contador de saques
    salvar_saldo()  # Salva o novo saldo no arquivo
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")  # Mensagem de sucesso

def exibir_extrato():
    """Exibe o extrato da conta, mostrando todas as movimentações e o saldo atual."""
    print("\n================ EXTRATO ================")  # Cabeçalho do extrato

    if not extrato:  # Verifica se o extrato está vazio
        print("Não foram realizadas movimentações.")  # Informa que não há transações registradas
    else:
        for operacao in extrato:  # Percorre a lista de transações e exibe cada uma
            print(operacao)

    print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual formatado com duas casas decimais
    print("==========================================")  # Rodapé do extrato

def main():
    """Função principal que controla o fluxo do programa."""
    carregar_saldo()  # Carrega o saldo do arquivo ao iniciar o programa

    while True:
        opcao = exibir_menu()  # Exibe o menu e recebe a opção do usuário

        if opcao == "d":
            depositar()  # Chama a função de depósito
        elif opcao == "s":
            sacar()  # Chama a função de saque
        elif opcao == "e":
            exibir_extrato()  # Chama a função de extrato
        elif opcao == "q":
            print("Saindo do sistema... Obrigado por usar nosso banco!")  # Mensagem de saída
            break  # Encerra o loop e finaliza o programa
        else:
            print("Operação inválida, por favor selecione novamente.")  # Mensagem de erro para opção inválida

# Inicia o programa somente se ele for executado diretamente (e não importado como módulo)
if __name__ == "__main__":
    main()
