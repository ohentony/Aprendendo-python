# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), 
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo 
# e use algumas dessas funções.
import moeda
valor = float(input('Digite um preço: R$'))
print(f'Aumentando 10%, temos R${moeda.aumentar(valor,10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(valor,10)}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'A metade de R${valor} é R${moeda.metade(valor)}')
