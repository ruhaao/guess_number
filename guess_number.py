import random

secret = random.randint(1, 100)

guess = int(input("Введите число от 1 до 100: "))

while guess != secret:
    if guess < secret:
        print('Ваше число меньше того, что загадано')
    else:
        print('Ваше число больше того, что загадано')
    guess = int(input("Введите число от 1 до 100: "))
   
   
print('Отличная интуиция! Вы угадали число :)')
