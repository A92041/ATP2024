# Gestão de sala de cinema

def inserirSala(cinema, sala):
    for s in cinema:
        if s[2] == sala[2]:  
            print(f"Sala para o filme '{sala[2]}' já existe.")
            return cinema
    cinema.append(sala)
    print(f"Sala para o filme '{sala[2]}' adicionada com sucesso.")
    return cinema

def listar(cinema):
    print("Filmes em exibição:")
    for sala in cinema:
        print(f" - {sala[2]}")  
    if not cinema:
        print("Não há filmes em exibição.")

def disponivel(cinema, filme, lugar):
    for sala in cinema:
        if sala[2] == filme:
            if lugar in sala[1]:  
                print(f"Lugar {lugar} já está ocupado para o filme '{filme}'.")
                return False
            elif lugar >= sala[0] or lugar < 0:  
                print(f"Lugar {lugar} é inválido para a sala de '{filme}'.")
                return False
            else:
                print(f"Lugar {lugar} está disponível para o filme '{filme}'.")
                return True
    print(f"Filme '{filme}' não encontrado.")
    return False


def vendebilhete(cinema, filme, lugar):
    for sala in cinema:
        if sala[2] == filme:
            if lugar in sala[1]: 
                print(f"Lugar {lugar} já está vendido para o filme '{filme}'.")
                return cinema
            elif lugar >= sala[0] or lugar < 0:  
                print(f"Lugar {lugar} é inválido.")
                return cinema
            else:
                sala[1].append(lugar)  
                print(f"Bilhete vendido para o lugar {lugar} do filme '{filme}'.")
                return cinema
    print(f"Filme '{filme}' não encontrado.")
    return cinema


def listardisponibilidades(cinema):
    print("Disponibilidade de lugares por filme:")
    for sala in cinema:
        disponiveis = sala[0] - len(sala[1])  
        print(f" - Filme: {sala[2]} | Lugares disponíveis: {disponiveis}")
    if not cinema:
        print("Não há filmes em exibição.")

def removerSala(cinema, filme):
    for i in range(len(cinema)):
        if cinema[i][2] == filme:
            del cinema[i]
            print(f"Sala do filme '{filme}' removida com sucesso.")
            return cinema
    print(f"Filme '{filme}' não encontrado.")
    return cinema

def menu():
    cinema = []  
    while True:
        print("\n--- Sistema de Gestão de Cinema ---")
        print("1. Inserir sala")
        print("2. Listar filmes em exibição")
        print("3. Verificar disponibilidade de lugar")
        print("4. Vender bilhete")
        print("5. Listar disponibilidade de lugares")
        print("6. Remover sala")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            filme = input("Digite o nome do filme: ")
            try:
                nlugares = int(input("Digite a lotação da sala: "))
                sala = [nlugares, [], filme]  
                cinema = inserirSala(cinema, sala)
            except ValueError:
                print("Erro: a lotação deve ser um número inteiro.")
        
        elif opcao == "2":
            listar(cinema)
        
        elif opcao == "3":
            filme = input("Digite o nome do filme: ")
            try:
                lugar = int(input("Digite o número do lugar: "))
                disponivel(cinema, filme, lugar)
            except ValueError:
                print("Erro: o número do lugar deve ser um número inteiro.")
        
        elif opcao == "4":
            filme = input("Digite o nome do filme: ")
            try:
                lugar = int(input("Digite o número do lugar: "))
                cinema = vendebilhete(cinema, filme, lugar)
            except ValueError:
                print("Erro: o número do lugar deve ser um número inteiro.")
        
        elif opcao == "5":
            listardisponibilidades(cinema)
        
        elif opcao == "6":
            filme = input("Digite o nome do filme para remover a sala: ")
            cinema = removerSala(cinema, filme)
        
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


menu()


