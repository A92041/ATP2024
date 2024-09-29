# Aplicação final da aula: 2024-09-23

def menu():
    print("Menu")
    print("1) pot(a,b)")
    print("2) divisao(a,b)")
    print("3) resto(a,b)")
    print("4) serie(b,s,n)")
    print("5) sair")

def pot(a, b):
    resultado = 1
    while b > 0:
        resultado = resultado * a
        b = b - 1

    return resultado

def divisao(a, b):
    resultado = 0
    while a >= b:
        resultado = resultado + 1
        a = a - b

    return resultado

def resto(a, b):
    while a >= b:
        a = a - b
    return a

def serie(base,salto,nelems):
    contador = 1
    while contador <= nelems:
        print(base, end = ", ")
        base = base + salto
        contador = contador + 1
    return

# ---------------------------
# Programa Principal
#
menu()
opcao = input("Selecione a opção desejada:")
while opcao != "5":
    if opcao == "1":
        num1 = int(input("Introduza um número inteiro (base):"))
        num2 = int(input("Introduza um número inteiro (expoente):"))
        print(f"O resultado é: {pot(num1,num2)}")

    elif opcao == "2":
        num1 = int(input("Introduza um número inteiro (dividendo):"))
        num2 = int(input("Introduza um número inteiro (divisor):"))
        print(f"O resultado é: {divisao(num1,num2)}")

    elif opcao == "3":
        num1 = int(input("Introduza um número inteiro (dividendo):"))
        num2 = int(input("Introduza um número inteiro (divisor):"))
        print(f"O resultado é: {resto(num1,num2)}")

    elif opcao == "4":
        num1 = int(input("Introduza um número inteiro (base):"))
        num2 = int(input("Introduza um número inteiro (salto):"))
        num3 = int(input("Introduza um número inteiro (nº de elementos):"))
        print(f"O resultado é: {serie(num1,num2,num3)}")
    else:
        opcao == "5"

    menu()
    opcao = input("Selecione a opção desejada:")
        
print("Obrigado, volte sempre!")
