from itertools import count

spb_price = 50_000
msc_price = 80_000
ekb_price = 40_000

print("Приветствую в системе помощи туриста!")
print("Доступные города: Питер, Москва, Екатеринбург")
city = input("Введите город: ")
count_people = int(input("Введите количество туристов: "))

if city == "Питер":
    total = spb_price * count_people
elif city == "Москва":
    total = msc_price * count_people
elif city == "Екатеринбург":
    total = ekb_price * count_people
else:
    print("Такого города нет")
    exit()

print("Вам нужно денег: " + str(total))