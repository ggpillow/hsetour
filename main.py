from itertools import count

spb_price = 50_000
msc_price = 80_000
ekb_price = 40_000

print("Приветствую в системе помощи туриста!")
print("Доступные города: Питер, Москва, Екатеринбург")
city = input("Введите город: ")
count_adult_people = int(input("Введите количество взрослых туристов: "))
count_kids_people = int(input("Введите количество детей: "))

if city == "Питер":
    total = spb_price * count_adult_people + spb_price * count_kids_people / 2
elif city == "Москва":
    total = msc_price * count_adult_people + msc_price * count_kids_people / 2
elif city == "Екатеринбург":
    total = ekb_price * count_adult_people + ekb_price * count_kids_people / 2
else:
    print("Такого города нет")
    exit()

print("Вам нужно денег: " + str(total))