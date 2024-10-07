#TPC4: Aplicação para manipulação de listas de inteiros

import random


def menu():
    print("Menu")
    print("1) Criar Lista ")
    print("2) Ler Lista ")
    print("3) Soma ")
    print("4) Média ")
    print("5) Maior")
    print("6) Menor")
    print("7) estaOrdenada por ordem crescente ")
    print("8) estaOrdenada por ordem decrescente ")
    print("9) Procura um elemento ")
    print("0) Sair ")

def criaLista():
    return [random.randint(1, 100) for _ in range(10)]  

def leLista():
    lista = []
    print("Insira os números (digite 'fim' para parar):")

    continuar = True
    while continuar:
        entrada = input("Digite um número: ")
        
        if entrada.lower() == 'fim':  # Se o usuário digitar "fim", altera a variável de controle
            continuar = False
        else:
            try:
                numero = int(entrada)
                lista.append(numero)
            except ValueError:
                print("Por favor, insira um número válido ou 'fim' para terminar.")
    
    return lista

def somaLista(lista):
    res = 0
    for x in lista: 
        res = res + x

    return res

def mediaLista(lista):
    return (somaLista(lista) / len(lista))

def maiorLista(lista):
    res = lista[0] #inicializamos com o primeiro elemento da lista = lista[0]
    for x in lista:
        if x > res:
            res = x
    return res

def menorLista(lista):
    res = lista[0] #inicializamos com o primeiro elemento da lista = lista[0]
    for x in lista:
        if x < res:
            res = x
    return res

def estaOrdenadaCD(lista, ordem):
    if ordem == "C":
        return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))
    elif ordem == "D":
        return all(lista[i] >= lista[i + 1] for i in range(len(lista) - 1))
    else:
        return False  # Retorna False se ordem não for "C" ou "D"
    
def procurar_elemento(lista, elemento):
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i  
    return -1  

# ---------------------------
# Programa Principal
#
menu()
opcao = input("Selecione a opção desejada:")
while opcao != "0":
    if opcao == "1":
        lista_numeros = criaLista()
        print("Lista criada:", lista_numeros)

    elif opcao == "2":
        lista_numeros = leLista()
        print("Lista criada:", lista_numeros)

    elif opcao == "3":
        print("Soma:", somaLista(lista_numeros))

    elif opcao == "4":
        media = mediaLista(lista_numeros)
        print("Média:", media)

    elif opcao == "5":
        maior = maiorLista(lista_numeros)
        print("Maior elemento:", maior)

    elif opcao == "6":
        menor = menorLista(lista_numeros)
        print("Menor elemento:", menor)

    elif opcao == "7":
        if estaOrdenadaCD(lista_numeros, ordem="C") == True:
               print("Está ordenada por ordem crescente")
        else: 
            print ("Está ordenada por ordem decrescente")

    elif opcao == "8":
        if estaOrdenadaCD(lista_numeros, ordem="C") == True:
               print("Está ordenada por ordem crescente")
        else: 
            print ("Está ordenada por ordem decrescente")
    
    elif opcao == "9":
            elemento = int(input("Digite o elemento que deseja procurar: "))
            posicao = procurar_elemento(lista_numeros, elemento)
            if posicao != -1:
                print(f"O elemento {elemento} está na posição {posicao}.")
            else:
                print(f"O elemento {elemento} não foi encontrado.")

    else:
        opcao == "0"

    menu()
    opcao = input("Selecione a opção desejada:")
        
print("Obrigado, volte sempre!")
