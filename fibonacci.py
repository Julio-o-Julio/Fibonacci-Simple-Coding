def whatToShow():

    print('Sequência de Fibonacci:')

    number = int(input('Em qual número você quer que a sequência de Fibonacci pare? '))
    
    counterZero = 0
    counterOne = 1

    while True:

        print(counterOne, end=', ')

        counter = counterZero + counterOne

        counterZero = counterOne

        counterOne = counter

        if counterOne > number:
            print()
            print(f'O último número da sequência antes de {number} é: {counterZero} ')
            break

whatToShow()

x = int(input('Quantos números você quer que a sequência de Fibonacci tenha? '))

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f'O {x}° número da sequência é: {fibonacci(x)}')
