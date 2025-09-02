''' peça ao usuario um numero maior que 10. repita enquanto o numero for menor ou igual a 10.'''

while True:
    try:
        numero = float(input("Escreva um número maior que 10:  "))
        if numero >=10:
           break
    except: print('por favor, insira um número válido!')

