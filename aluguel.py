km= float(input('Digite aqui quantos kms você percorreu:'))
dias= int(input('Digite aqui quantos dias você ficou com o carro:'))
km_valor= km*0.15
dia_valor= dias*60
total= km*0.15+dias*60
print(f'Você percorreu um total de {km}km e o valor ficará R${km_valor:.2f}')
print(f'Você ficou com o carro {dias} dias e o valor será R${dia_valor:.2f}')
print(f'O valor total será R${total:.2f}!')
print('Obrigado por ser nosso cliente!')

# escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0.15 por Km rodado.
