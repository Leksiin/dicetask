import random

def tilda():
    print("~" * 40)

def get_number(prompt):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("ОШИБКА: Поле не может быть пустым.")
            continue
        try:
            number = int(value)
            if number < 1:
                print("ОШИБКА: Число должно быть больше нуля.")
                continue
            return int(value)
        except ValueError:
            print("ОШИБКА: Поле не должно содержать букв и прочих символов.")

# Ввод данных
tilda()
k = get_number("Количество игральных кубиков (Введите число): ")
tilda()
a = get_number("A - Максимальная сумма очков: ")
b = get_number("B - Максимальное произведение очков: ")
c = get_number("C - На что делиться произведение: ")

n = 1000 # Кол-во опытов

count_A = 0
count_B = 0
count_C = 0

# Симуляция бросков
for _ in range(n):
    sum_dice = 0
    prod_dice = 1

    for _ in range(k):
        dice = random.randint(1, 6)
        sum_dice += dice
        prod_dice *= dice

    if sum_dice <= a:
        count_A += 1
    if prod_dice <= b:
        count_B += 1
    if prod_dice % c == 0:
        count_C += 1

# Вывод результатов
tilda()
print(f"Результаты для {n} опытов с {k} игральными кубиками")
tilda()
print(f"Вероятность A (сумма не превосходит {a}): {count_A / n:.4f}")
print(f"Вероятность B (произведение не превосходит {b}): {count_B / n:.4f}")
print(f"Вероятность C (произведение делится на {c}): {count_C / n:.4f}")
tilda()
print("Решение")
print("Формула: P=m/n")
tilda()
print(f"Вероятность A: P={count_A}/{n}")
print(f"Вероятность B: P={count_B}/{n}")
print(f"Вероятность C: P={count_C}/{n}")
tilda()
