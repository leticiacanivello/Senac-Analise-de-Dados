nota1 = float(input('digite sua nota de portugues: '))
nota2 = float(input('digite sua nota de matematica: '))
nota3 = float(input('digite sua nota de geografiia: '))
nota4 = float(input('digite sua nota de artes: '))
média = float ((nota1 + nota2 + nota3 + nota4 ) / 4 )
print(f'o seu resultado é')

if média >= 7:
    print ('aprovado!')
elif 5<= média <7:
    print ('em recuperação')
elif média <5:
    print('reprovado')