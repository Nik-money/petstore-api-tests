# Простой пример цикла While
def while_cycle_1():
    number = 1
    while number <= 5:
        print(f'number = {number}')
        number += 1
    print('Работа программы завершена')

# While c else:
def while_cycle_2():
    number = 1
    while number < 5:
        print(f"number = {number}")
        number += 1
    else:
        print(f"number = {number}. Работа цикла завершена")
    print("Работа программы завершена")

# Else при изначально ложном условии:
def while_cycle_3():
    number = 10
    while number < 5:
        print(f"number = {number}")
        number += 1
    else:
        print(f"number = {number}. Цикл пропущен")
    print("Работа программы завершена")

# Цикл for
def for_cycle_1():
    message = 'Hello'
    for letter in message:
        print(letter)

# Цикл for -> перебор списка:
def for_cycle_2():
    fruits = ['apple', 'banana', 'orange']
    for fruit in fruits:
        print(f'Фрукт: {fruit}')

# Цикл for -> с функицей range() генерация числовых последовательностей:
# range с одним параметром (от 0 до stop-1)
def for_cycle_3():
    for num in range(5):
        print(num, end= ' ') # 0 1 2 3 4

# range с двумя параметрами (start, stop)
def for_cycle_4():
    for num in range(2, 6):
        print(num, end= ' ') # 2 3 4 5
# range с тремя параметрами (start, stop, step)
def for_cycle_5():
    for num in range(1,10,2):
        print(num, end= ' ') # 1 3 5 7 9

# обратный порядок (отрицательный step)
def for_cycle_6():
    for num in range(1,10, -2):
        print(num, end= ' ') # 10 8 6 4 2

# for c else
def for_cycle_7():

    message = 'Hello'
    letter = message[0] # можно не создавать, for автоматически создает переменную
    for letter in message:
        print(letter)
    else:
        print(f'Последний символ = {letter}. Цикл завершен')
    print('Работа программы завершена')

# Сравнение while и for для решения 1 задачи:
# Задача. Вывести числа от 1 до 5

# Решение. С while
def task_1():
    i = 1
    while i <= 5:
        print(i, end= ' ')
        i += 1

# Решение. С for
def task_2():
    for i in range(1, 6):
        print(i, end= ' ')

# Вложенные циклы (nested loops)
# Таблица умножения с while:
def while_cycle_4():
    i = 1
    j = 1
    while i < 10:
        while j < 10:
            print(i * j, end= '\t')
            j += 1
        print('\n')
        j = 1
        i += 1

# Таблица умножения с for
def for_cycle_8():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i *j , end= '\t')
        print()

# Комбинации символов for
def for_cycle_9():
    for c1 in 'ab':
        for c2 in 'ba':
            print(f'{c1}{c2}')

# Управление циклами break и continue
# break - полный выход из цикла.
def while_cycle_5():
    number = 0
    while number < 5:
        number += 1
        if number == 3: # Выход из цикла при number == 3
            break
        print(f'Число = {number}')
    print('Цикл завершен')

# continue -> переход к следующей итерации
def while_cycle_6():
    number = 0
    while number < 5:
        number += 1
        if number == 3: continue # пропускаем печать для number 3
        print(f'Число = {number}')
    print('Цикл завершен')

# Примеры использования:
# break: поиск первого отрицательного числа
def for_cycle_10():
    numbers = [5, 3, 8, -2, 9, 1]
    for num in numbers:
        if num < 0:
            print(f'Найдено отрицательное число: {num}')
            break

# continue: печатаем только ЧЕТНЫЕ числа
def for_cycle_11():
    for num in range(1, 10):
        if num % 2 != 0: continue
        print(num, end= ' ')

if __name__ == "__main__":
    for_cycle_11()