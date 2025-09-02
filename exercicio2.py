"""desenvolva um programa que receba o nome, ano e as notas do aluno. 
Caso o usuário digitar algo errado, peça que digite novamente 
até ele digitar o dado correto. 
Ao final, exiba em uma unica mensagem o nome do aluno com sua situação final."""

while True:
    try:
        nome_aluno = str(input('informe seu nome: '))
        break
    except:
        print('por favor, digite um nome válido! ')
while True:
    try:
        ano_escolar = int(input('ótimo! agora informe seu ano escolar: '))
        break
    except:
        print('por favor, digite um ano escolar válido! ')
while True:
    try:
        nota1 = float(input('agora vamos ver suas notas! digite sua nota de portugues: '))
        break 
    except:
        print('por favor, insira um número válido!')
while True:
    try:
        nota2 = float(input('digite sua nota de matematica: '))
        break
    except:
        print('por favor, insira um número válido!')
while True:
    try:
        nota3 = float(input('digite sua nota de geografiia: '))
        break
    except: print('por favor, insira um número válido!')
while True:
    try:
        nota4 = float(input('digite sua nota de artes: '))
        break
    except: print('por favor, insira um número válido!') 
média = float ((nota1 + nota2 + nota3 + nota4 ) / 4 )
print(f'{nome_aluno} , sua situação final é: {média}')
if média >= 7:
    print ('aprovado!')
elif 5<= média <7:
    print ('em recuperação')
elif média <5:
    print('reprovado')