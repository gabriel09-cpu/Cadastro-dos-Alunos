# Função que exibe o menu principal do sistema
def menu_inicial(): 
    print("1. Adicionar aluno")
    print("2. Ver Boletim de todos os alunos")
    print("3. Buscar aluno pelo nome")  # Tem um errinho de digitação: "qluno" → "aluno"
    print("4. Sair")

# Dicionário com os nomes dos alunos como chaves e listas de notas como valores
alunos = {
    "Gabriel": [7.5, 8.0, 9.0, 5.5],
    "Laura": [4.5, 8.5, 7.5, 9.0],
    "Sandra": [6.5, 7.5, 9.0, 10.0],
    "Gabriela": [10.0, 10.0, 10.0, 9.5],
    "Fernando": [6.0, 8.0, 7.0, 5.5],
    "Bernardo": [5.0, 7.5, 4.0, 10.0]
}

# Loop principal do programa: será executado até que o usuário escolha sair
while True:
    menu_inicial()  # Mostra o menu para o usuário

    # Solicita uma opção e converte para inteiro
    opcao = int(input("Bem-Vindo! O que posso fazer por você hoje? "))

    # Opção 1: Adicionar novo aluno
    if opcao == 1:
        novatos = input("Informe o nome do novo aluno: ")
        
        if novatos in alunos:  # Verifica se o aluno já está cadastrado
            print("Aluno já cadastrado!")
        else:
            alunos[novatos] = []  # Cria uma nova entrada no dicionário com lista de notas vazia

    # Opção 2: Exibir o boletim completo (todos os alunos e suas notas)
    elif opcao == 2:
        print(alunos)  # Mostra o dicionário completo (forma simples)

    # Opção 3: Buscar aluno pelo nome
    elif opcao == 3:
        # Recebe o nome e usa .capitalize() para padronizar a entrada
        busca = str(input("Digite o nome do Aluno: ")).capitalize()

        if busca in alunos:  # Verifica se o nome existe no dicionário
            print(f"As nota de {busca}: {alunos[busca]}")  # Exibe as notas do aluno
        else: 
            print(f"{busca} não encontrado na nossa base de dados!😒")  # Mensagem de erro se não achar o aluno

    # Opção 4: Sair do programa
    elif opcao == 4:
        print("Tenha um bom dia!")
        break  # Encerra o laço while e finaliza o programa
