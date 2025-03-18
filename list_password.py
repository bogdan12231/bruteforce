from itertools import product

# Генерируем все комбинации из 6 цифр (от 000000 до 999999)
all_passwords = [''.join(p) for p in product('0123456789', repeat=6)]

# Проверяем количество паролей
print(f"Всего паролей: {len(all_passwords)}")  

# Выводим первые 10 паролей для примера
print(all_passwords[:10])