"""3) um motorista de táxi deseja calcular o rendimento de seu carro ao
final do dia. Desenvolva um programa que receba:
- A marcação do odômetro no início e no fim do dia (em km),
- A quantidade de litros de combustível consumidos,
- O valor total recebido dos passageiros (em reais).

Sabendo que o preço do combustível é R$ 4,87 por litro, o programa
deve calcular:

- A média de consumo (km por litro),

- O gasto com combustível,

- O lucro líquido do dia (valor recebido - gasto com combustível).
"""

od_inicio = float(input("Inisira a marcação do odômetro no inicio do dia:  "))
od_fim = float(input("Insira a marcação do odômetro no fim do dia:  "))

comb_consumido = float(input("Insira a quantidade de litros de combustivel consumido: "))

vt_passageiros = float(input( "Insira o valor total recebido de seus passageiros:  "))

preço_litro_combustivel = float(4.87)

media_consumo = (od_fim - od_inicio) / comb_consumido

gasto_combustivel = comb_consumido * preço_litro_combustivel 

lucro_liquido = vt_passageiros - gasto_combustivel 

print(f" A média de consumo de combustivel é de {media_consumo:.2f} km/l, o gasto com combustivel foi de {gasto_combustivel:.2f} reais e o lucro liquido do dia foi de {lucro_liquido:.2f} reais.")