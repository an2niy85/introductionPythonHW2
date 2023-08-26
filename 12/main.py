# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

import random

x = random.randint(0,1001)
y = random.randint(0,1001)

print('Угадай два числа')
print('Их сумма равна ' + str(x + y))
print('А произвежение = ' + str(x * y))
isGuess = True
countAttempt = 5
while (isGuess and countAttempt > 0):
    x0 = int(input('Первое число: '))
    y0 = int(input('Второе число: '))
    if x0+y0 == x + y and x0*y0 == x * y:
        print(f'Угадал! Первое число = {x0}, второе = {y0}.')
        isGuess = False
    elif countAttempt > 1:
        print('Не угадал. Попробуй еще...')
    countAttempt -= 1        
else:
    if (countAttempt == 0):
        print('К сожалению попыток не осталось')
    print(f'Были загаданы числа {x} и {y}.')