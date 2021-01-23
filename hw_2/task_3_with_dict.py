seasons = dict(winter=(1, 2, 12), spring=(3, 4, 5), summer=(6, 7, 8), autumn=(9, 10, 11))
print(seasons.values())
print(seasons.keys())
user_answer = int(input('Введите месяц в виде целого числа от 1 до 12: '))

for el in seasons.items():
    for num in el[1]:
        if num == user_answer and el[0] == 'winter':
            print(f"Месяц под номером №{user_answer} относится к зиме.")
        elif num == user_answer and el[0] == 'spring':
            print(f"Месяц под номером №{user_answer} относится к весне.")
        elif num == user_answer and el[0] == 'summer':
            print(f"Месяц под номером №{user_answer} относится к лету.")
        elif num == user_answer and el[0] == 'autumn':
            print(f"Месяц под номером №{user_answer} относится к осени.")
