print('Приветствую, давайте создадим список товаров с характеристиками.')

char = []
name = []
price = []
quantity = []
unit = []

all_list = [name, price, quantity, unit]

products = dict(Название='name', Цена='price', Количество='quantity', Ед='unit')
products['Название'] = input('Введите название: ')
name.append(products['Название'])
products['Цена'] = input('Введите цену: ')
price.append(products['Цена'])
products['Количество'] = input('Введите количество: ')
quantity.append(products['Количество'])
products['Ед'] = input('Введите единицу измерения: ')
unit.append(products['Ед'])

for el in products.keys():
    char.append(el)

copy_prod = products.copy()
pos = 0
num = 1
user_list = (num, copy_prod)

full_list = []
full_list.insert(pos, user_list)

answer = dict()

print(full_list)

# for el in char:
#     answer = dict(char[pos]:)
#     pos += 1

while True:

    continue_check = input("Продолжим? (Yes - Да; No - Нет)\nПосле ввода 'No' программа "
                           "автоматичски соберет аналитику о товарах.': ")

    if continue_check == 'No':

        for el in copy_prod.values():
            answer.update({char[0]: name})
            answer.update({char[1]: price})
            answer.update({char[2]: quantity})
            answer.update({char[3]: unit})

        print(answer)

        break

    elif continue_check == 'Yes':
        num += 1
        pos += 1
        products['Название'] = input('Введите название: ')
        name.append(products['Название'])
        products['Цена'] = input('Введите цену: ')
        price.append(products['Цена'])
        products['Количество'] = input('Введите количество: ')
        quantity.append(products['Количество'])
        products['Ед'] = input('Введите единицу измерения: ')
        unit.append(products['Ед'])

        copy_prod = products.copy()
        user_list = (num, copy_prod)

        full_list.insert(pos, user_list)

        print(full_list)