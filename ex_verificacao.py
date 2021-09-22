verificacao = False #Não utilizado neste exemplo, apenas utilizado quando não tem break

while True:
    
    n1 = input('Informe o primeiro valor: ')
    if n1.isnumeric():
        n2 = input('Informe o segundo valor: ')
        if n2.isnumeric():
            n1 = float(n1)
            n2 = float(n2)
            resultado = (n1+n2)/2
            break
    print('Por favor informe um valor numerico...')

print(f'A média entre os números {n1} e {n2} é igual a {resultado}!')
