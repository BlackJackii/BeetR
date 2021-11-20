# elem1 = "#"*9+"\n"
# elem2 = "#"+" "*7+"#"+"\n"
# print(elem1 + elem2*3 + elem1 + "\n" + elem2*2 + elem1 + elem2*2)

# total = 44
# rez = round(total*0.8)
# print("Для успешного окончания курса надо сдать {} домашек".format(rez))
# assert rez ==35
#
# x1 = int(input("x1 = "))
# y1 = int(input("y1 = "))
# x2 = int(input("x2 = "))
# y2 = int(input("y2 = "))
# distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
# print(distance)

# var1 = 'pyThoN'
# var1 = var1.title()
# assert var1 == 'Python'
# var1 = var1.upper()
# assert var1 == 'PYTHON'
# var1 = var1.lower()
# assert var1 == 'python'
# var1 = " python "
# var1 = var1.strip()
# assert var1 == 'python'

# name = "Остап"
# print("Привет {} ".format(name))
#
# name = "Остап"
# print(f"Привет {name}")
#
# name = "Остап"
# print("Привет %name")
#
# price = 12
# weight = 3.4121
# rez = 0
# ans = price * weight
# ans = round(ans, 2)
# rez = f'Итого: {ans}'
# print(rez)
# assert rez == 'Итого: 40.95'

# number = 12
# username = "ираклий"
# access_mask = 54
# hour_price=15.321
# rez = 0
#
# rez = "0000"+str(number), username.title(), access_mask, round(hour_price, 2)
# print(rez)
# assert  rez == '000012 Ираклий 110110 15.32'



# base_str = 'Корова'
# rez = 0
# rez = "В"+base_str[1:4]+"на"
# print(rez)
# assert rez == 'Ворона'


# a = 10
# b = 55
# c = b
# b = a
# a = c
# assert a==55 and b==10, "Не поменялось. :("