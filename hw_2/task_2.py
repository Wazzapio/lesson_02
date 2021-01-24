my_list = []
num = 1
ind_0 = 0
ind_1 = 1


print("Приветствую, давайте создадим список из эл-тов.")
num_max = int(input('Укажите количество эл-тов: '))

while len(my_list) < num_max:
    el = input(f"{num}-й элемент: ")
    my_list.append(el)
    num += 1

print(my_list)

print("\nА теперь поменяем значения элементов с индексами 0 и 1, а так же 2 и 3 и т.д.")

while ind_1 != len(my_list):
    my_list[ind_0], my_list[ind_1] = my_list[ind_1], my_list[ind_0]
    ind_0 += 2
    ind_1 += 2


