my_string = input("Введите несколько слов через пробел: ")
num = 1
for word in my_string.split():
    print(f"№{num}:", word[:10])
    num += 1
