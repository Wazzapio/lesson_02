winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
seasons = [winter, spring, summer, autumn]

user_answer = int(input('Введите месяц в виде целого числа от 1 до 12: '))

for name in seasons:
    for el in name:
        if el == user_answer and name == seasons[0]:
             print(f"Месяц под номером №{user_answer} относится к зиме.")
        elif el == user_answer and name == seasons[1]:
             print(f"Месяц под номером №{user_answer} относится к весне.")
        elif el == user_answer and name == seasons[2]:
             print(f"Месяц под номером №{user_answer} относится к лету.")
        elif el == user_answer and name == seasons[3]:
             print(f"Месяц под номером №{user_answer} относится к осени.")


