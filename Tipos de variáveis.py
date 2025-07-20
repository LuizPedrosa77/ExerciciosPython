''''
numero_geral = 10
def imprime_local():
    numero = 5
    print(numero)
imprime_local()
print(numero_geral)

# Exemplo de variavel global e local
cliente = "Luiz"
passo = 0
status = "Aguardando novo pedido"

def atender():
    global passo
    passo += 1
    status = "Pedido recebido."
    print(f"Passo {passo}: {status}")
    preparar()
    
def preparar():
    global passo
    passo += 1
    status = "Preparando..."
    print(f"Passo {passo}: {status}")
    entregar
    
def entregar():
    global passo 
    passo += 1
    status = "Pedido entrege"
    print(f"Passo {passo}: {status} ao {cliente}!")
    
atender()
preparar()
entregar()
print(status)
'''


num1 = 0.0
num2 = 0.0
num3 = 0.0

def ler_numero():
    global num1, num2, num3
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    num3 = float(input("Digite o terceiro numero: "))
    print(f"Os números lidos são: {num1}, {num2}, {num3}.")

def calcular_soma():
    soma = num1 + num2 + num3
    print(f"A soma é: {soma}.")
    
def calcular_media():
    media = (num1 + num2 + num3) / 3
    print(f"A média é: {media}.")
    
ler_numero()
calcular_soma()
calcular_media()
