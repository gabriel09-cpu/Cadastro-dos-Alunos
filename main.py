def menu_inicial():
    print("1. Adicionar aluno")
    print("2. Ver Boletim de todos os alunos")
    print("3. Buscar qluno pelo nome")
    print("4. Sair")
    
alunos = {
    "Gabriel": [7.5, 8.0, 9.0, 5.5],
    "Laura": [4.5, 8.5, 7.5, 9.0],
    "Sandra": [6.5, 7.5, 9.0, 10.0],
    "Gabriela": [10.0, 10.0, 10.0, 9.5],
    "Fernando": [6.0, 8.0, 7.0, 5.5],
    "Bernardo": [5.0, 7.5, 4.0, 10.0]
}



while True:
    menu_inicial()
    opcao = int(input("Bem-Vindo! O que posso fazer por você hoje? "))
    if opcao == 1:
        novatos = input("Informe o nome do novo aluno: ")
        
        if novatos in alunos:
            print("Aluno já cadastrado!")
        else:
            alunos[novatos] = []
    elif opcao == 2:
        print(alunos)
    
    elif opcao == 3:
        busca = str(input("Digite o nome do Aluno: ")).capitalize()
        if busca in alunos:
            print(f"As nota de {busca}: {alunos[busca]}")
        else: 
            print(f"{busca} não encontrado na nossa base de dados!😒")
    elif opcao == 4:
        print("Tenha um bom dia!")
        break