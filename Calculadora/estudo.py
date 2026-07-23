# Calculadora
print('                        Calculadora Píton\n')

while True:
    try:
        n1 = int(input('Digite um número: '))
        n2 =  int(input('Digite outro número: '))
        break
    except ValueError:
        print('APENAS NÚMEROS!')
while True:
    operator = str(input('Qual operador aritmético você deseja usar? '))

    print('+', '-', '/', '*')
    print('Digite "SAIR" caso queira sair da calculadora. ')

    if operator == '+':
        s = n1 + n2
        print(s)

    elif operator == '-':
        subt = n1 - n2
        print(subt)

    elif operator == '*':
        mult = n1 * n2
        print(mult)
    
    elif operator == '/':
        div = n1 / n2
        print(div)

    elif operator == 'SAIR':
        print('Tchau.')
        break
    


