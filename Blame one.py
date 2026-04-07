import math
import random

print("Завдання 1")
try:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    print(f"Результат: {a / b}")
except ValueError:
    print("Помилка: введене значення не є числом")
except ZeroDivisionError:
    print("Помилка: ділення на нуль")
finally:
    print("Операцію завершено")

print("\nЗавдання 2")
lst = [10, 20, 30, 40, 50]
print(f"Список: {lst}")
try:
    index = int(input("Введіть індекс елемента: "))
    print(f"Елемент: {lst[index]}")
except ValueError:
    print("Помилка: індекс не є числом")
except IndexError:
    print("Помилка: індекс виходить за межі списку")
finally:
    print("Операцію завершено")

print("\nЗавдання 3")
try:
    data = input("Введіть дані про продажі через пробіл: ")
    sales = [float(x) for x in data.split()]
    print(f"Загальна сума продажів: {sum(sales)}")
except ValueError:
    print("Помилка: некоректне введення")
finally:
    print("Обробку завершено")

print("\nЗавдання 4")
try:
    number = float(input("Введіть число: "))
    if number < 0:
        raise Exception("Не можна обчислити квадратний корінь від'ємного числа")
    print(f"Квадратний корінь: {math.sqrt(number)}")
except ValueError:
    print("Помилка: введене значення не є числом")
except Exception as e:
    print(f"Помилка: {e}")
finally:
    print("Обчислення завершено")

print("\nЗавдання 5")
try:
    data = input("Введіть дані про товар (назва, ціна, кількість): ")
    parts = data.split(",")
    name = parts[0].strip()
    price = float(parts[1].strip())
    quantity = int(parts[2].strip())
    print(f"Товар: {name}, ціна: {price}, кількість: {quantity}, сума: {price * quantity}")
except ValueError:
    print("Попередження: некоректні дані, неможливо перетворити ціну або кількість")
finally:
    print("Парсинг завершено")

print("\nЗавдання 6")
def connect_to_server():
    if random.choice([True, False]):
        return "Підключення успішне"
    else:
        raise ConnectionError("Помилка підключення")

try:
    result = connect_to_server()
    print(result)
except ConnectionError:
    print("Не вдалося підключитися до сервера")
finally:
    print("Спробу завершено")