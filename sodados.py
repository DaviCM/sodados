import os
import random as rd

def ChecarValores(value):
    if (value.strip()).isnumeric() == False or value.strip() == "0":
        return False, None
    else:
        return True, int(value.strip())        
 
 
def PegarDados(msg):
    diceinfo = input(msg)
    valid, diceinfo = ChecarValores(diceinfo)
    while valid == False:
        diceinfo = input("Por favor, insira um valor natural diferente de 0: ")
        valid, diceinfo = ChecarValores(diceinfo)    
    return diceinfo  

    
def RolarDados():
    dicenum = PegarDados("Quantos dados você quer gerar? ")
    diceside = PegarDados("Com quantos lados? ")
    
    # List comprehension para gerar uma lista com todos os resultados de forma fácil, para poder imprimir em sequência e somar. '_' avisa que o valor dessa iteração não importa para o código.
    results = [rd.randint(1, diceside) for _ in range (1, dicenum + 1)]     # O loop for por padrão inicia do 0, então tenho que adicionar 1 pra compensar o valor a menos que ele rolaria.

    for i, xresult in enumerate(results, start=1):      # Esse for loop armazena um valor 'i' para a posição de cada valor extraido pela tupla (enumerate) e um valor 'xresult' para o valor em si.
        # Ex: results = [1, 4, 5]
        # enumerate(results) = [(results[0], 1), (results[1], 4), (results[2], 5)] - inicia pelo 0 como default, mas pode ser mudado com o parâmetro start
        # i = [0, 1, 2] - Método de desempacotar tupla com loop for, gerando uma lista
        # xresult = [1, 4, 5] - Método de desempacotar tupla com loop for, gerando uma lista
        
        print(f"O {i}° d{diceside} teve valor de {xresult}.")
        
    print(f"A soma dos valores de {dicenum}d{diceside} foi: {sum(results)}.")

quit = input("Bem vindo ao gerador de dados! Aperte qualquer tecla para iniciar. (Aperte 'N' para sair.) ")

while not "N" in quit.upper():
    print("AVISO: O Programa apenas aceita dados de valores naturais diferentes de 0.")   
    RolarDados()
    quit = input("Aperte qualquer tecla para rolar mais dados! ('N' para sair.) ")
    os.system("cls" if os.name == "nt" else "clear")
    
