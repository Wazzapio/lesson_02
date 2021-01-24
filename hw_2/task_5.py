my_list = [7, 5, 3, 3, 2]

print('Приветствую, давайте реализуем структуру "Рейтинг" данного списка:')
print(my_list)
num = input("Ведите число: ")

while num != 'q':
    pos = 0
    x = 0

    for el in list(my_list):
        if int(num) > el:
            my_list.insert(pos, int(num))
            break
        elif int(num) < el:
            pos += 1
    if pos == len(my_list):
        my_list.insert(pos, int(num))

    print(my_list)
    print('Для того чтобы выйти из цикла введите "q"')
    num = input("Давайте добавим еще число: ")

print('Вы вышли из программы.')
