nExtenso012 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze')
nExtenso1320 = ('Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
nExtenso020 = nExtenso012 + nExtenso1320
while True:
    n = int(input('Digite um inteiro de 0 a 20: '))
    while not 0 <= n <= 20:
        n = int(input('Número inválido. Digite novamente um número inteiro de 0 a 20: '))
    print(f'Você digitou o número: \033[1m{nExtenso020[n]}\033[m')
    c = input('Deseja continuar (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar (S/N)? ').strip()[0]
    if c in 'nN':
        break





