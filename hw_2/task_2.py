my_list = []
num = 1
print("Приветствую, давайте создадим список из 4-ех эл-тов.")

while len(my_list) < 4:
    el = input(f"{num}-й элемент: ")
    my_list.append(el)
    num += 1

print(my_list)

print("\nА теперь поменяем значения элементов с индексами 0 и 1, а так же 2 и 3.")

my_list[0], my_list[1] = my_list[1], my_list[0]
my_list[2], my_list[3] = my_list[3], my_list[2]

print(my_list)


