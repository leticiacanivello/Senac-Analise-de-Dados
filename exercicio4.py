"""Em uma turma, os alunos realizam duas avaliações principais e têm a opção
de fazer uma terceira avaliação (optativa), que pode substituir a nota mais baixa.
Escreva um programa que receba:
- Nota da primeira avaliação,
- Nota da segunda avaliação,
- Nota da avaliação optativa (ou -1 caso não tenha feito).
O programa deve calcular a média do semestre considerando a substituição da
menor nota, se a optativa for válida. Depois, deve exibir:
- A média final,
- Uma mensagem indicando a situação do aluno:
- Aprovado: média ≥ 6.0
- Reprovado: média < 3.0
- Exame: média ≥ 3.0 e < 6.0"""

print("Olá, aluno! Insira abaixo as notas das suas avaliações para saber seu resultado final!")
nota1 = float(input( "Escreva a nota da sua primeira avaliação:  "))
nota2 = float(input("Escreva a nota da sua segunda avaliação:  "))
nota_optativa = float(input( "Escreva a nota da sua avaliação optativa. Caso não tenha feito, responda: -1  :"))
match nota_optativa:
    case -1:
        media = (nota1 + nota2) / 2
    case nota_optativa if nota_optativa > nota1: 
        media = (nota_optativa + nota2) / 2
    case nota_optativa if nota_optativa > nota2:
        media = (nota1 + nota_optativa) / 2 

match media:
    case media if media >= 6.0: 
        print (f"Sua média  final é {media} e você está aprovado! ")
    case media if media < 3.0:
        print (f"Sua média final é {media} e você está reprovado. ")
    case _ : 
        print (f"Sua média final pe {media} e você está de recuperação.")
    