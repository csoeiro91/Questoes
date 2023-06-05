#Questão 3 - IF e Else
def funcao_a(num):
    if num > 0:
        print("Função A chamada!")
        funcao_b(num)
    else:
        print("Função A terminada.")

def funcao_b(num):
    if num > 0:
        print("Função B chamada!")
    else:
        print("Função B terminada.")

print(funcao_a(3))







##### Questão 4 - For #####
def imprimir_numeros(n):
# i = 0
    for i in range(n):
        print(i)

imprimir_numeros(5)






##### Questão 5 - While #####
def MetodoWhile():
    contador = 1
    while contador <= 10:
        print(contador)
        contador += 1


print(MetodoWhile())






