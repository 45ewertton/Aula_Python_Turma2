'''
Conversões: str, int, float, bool, list, tuple e ...

n = str(5)
print(type(n))
print(n)

'''

#######################################################################

'''
Entrada de dados: input():

nome = input("Diga seu nome: ")
print(type(nome))
print("Meu nome é : " + nome)
'''

########################################################################

'''
Estruturas condicionais if, else e elif.

numero = 10

if numero > 10:
    print('Estou dentro do if')

print('Estou fora do if')

--------------------------------------------------------

idade = 18

if idade >= 18:
    print(f'Tenho {idade} anos, sou maior de idade.')
else:
    print(f'Tenho {idade} anos, sou menor de idade.')

---------------------------------------------------------

idade = -1

if idade < 0:
    print('Digite um valor válido...')

elif idade >= 0 and idade < 16:
    print('Não pode votar!')   

elif idade <= 17 or idade > 70:
    print('Voto não é obrigatório')

else:
    print('Voto obrigatório')
'''

################################################################################

'''
Estruturas de repetições while e for. Possível passar o continue e break

i = 1

while i <= 6:
  print(i)
  i = i + 1

-------------------------------------------------------------

for i in 'banana':
    print(i)

lista = ['banana', 'maçã', 22, ['melancia', 99.23]]
for item in lista:
    print(item)

for i in range (2, 30, 2):
    print(i)
'''

##########################################################################################

'''
Estruturas de dados, lista, pilha e fila.

lista = [1, 'Maria' True]
print(lista)
---------------------------------------------------------------------

pilha = [1, 2]
pilha.append(3)
pilha.pop()
print(pilha)

---------------------------------------------------------------------



'''