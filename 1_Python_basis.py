# Строчные / прописные

name = "иван иваныч иванов"
print(name)

# первые заглавные
name = name.title()
print(name)

# все заглавные
name = name.upper()
print(name)

# все прописные
# предпочительный вариант: перед сохранением данных, всё перевести в нижний регистр. Перед выводом использовать нужный регистр
name = name.lower()
print(name)

# удаление пробелов в начале / конце строки
name = " Nata "
print(f"'{name}'")

name = " Nata "
name = name.rstrip()  # удаление пробела в конце
print(f"'{name}'")

name = " Nata "
name = name.lstrip()  # удаление пробела в начале
print(f"'{name}'")

name = " Nata "
name = name.strip()  # удаление пробела с обеих сторон
print(f"'{name}'")

# обрезка знаков после запятой
a = 0.2456
b = 3
c = round(a * b, 2)
print(c)

print (1 + 2.0)