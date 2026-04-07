print("Завдання 1")
try:
    price = float(input("Введіть початкову ціну: "))
    discount = float(input("Введіть відсоток знижки: "))
    final_price = price - (price * discount / 100)
    print(f"Фінальна ціна: {final_price}")
except ValueError:
    print("Помилка: введене значення не є числом")

print("\nЗавдання 2")
try:
    dollars = float(input("Введіть суму в доларах: "))
    rate = float(input("Введіть курс обміну на євро: "))
    if rate == 0:
        raise Exception("Курс обміну не може дорівнювати нулю")
    euros = dollars * rate
    print(f"Сума в євро: {euros}")
except ValueError:
    print("Помилка: некоректне введення")
except Exception as e:
    print(f"Помилка: {e}")
finally:
    print("Операцію завершено")

print("\nЗавдання 3")
try:
    data = input("Введіть оцінки через пробіл: ")
    grades = [float(x) for x in data.split()]
    average = sum(grades) / len(grades)
    print(f"Середнє значення: {average}")
except ValueError:
    print("Помилка: одне з введених значень не є числом")
except ZeroDivisionError:
    print("Помилка: список оцінок порожній")
finally:
    print("Завершення обчислень")

print("\nЗавдання 4")
balance = 1000
try:
    amount = float(input(f"Введіть суму для зняття (баланс: {balance}): "))
    if amount % 10 != 0 or amount > balance:
        raise Exception("Некоректна сума для зняття")
    balance -= amount
    print(f"Знято: {amount}. Залишок: {balance}")
except ValueError:
    print("Помилка: некоректне введення")
except Exception as e:
    print(f"Помилка: {e}")
finally:
    print("Транзакцію завершено")

print("\nЗавдання 5")
try:
    order = input("Введіть номер замовлення: ")
    if not order.startswith("ORD") or not order[3:].isdigit() or len(order[3:]) == 0:
        raise Exception("Неправильний формат номера замовлення")
    print(f"Номер замовлення {order} коректний")
except Exception as e:
    print(f"Помилка: {e}")
finally:
    print("Перевірку завершено")

print("\nЗавдання 6")
try:
    data = input("Введіть послідовність чисел через пробіл: ")
    elements = data.split()
    numbers = []
    for element in elements:
        try:
            numbers.append(float(element))
        except ValueError:
            print(f"Попередження: '{element}' не є числом, пропускаємо")
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Сума: {total}, Середнє: {average}")
except ZeroDivisionError:
    print("Помилка: список виявився порожнім")
finally:
    print("Обробку даних завершено")