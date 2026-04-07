import random

def power(number, degree):
    if degree == 0:
        return 1
    return number * power(number, degree - 1)

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(month, year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days[month - 1]

def date_to_days(day, month, year):
    total = 0
    for y in range(1, year):
        if is_leap_year(y):
            total += 366
        else:
            total += 365
    for m in range(1, month):
        total += days_in_month(m, year)
    total += day
    return total

def difference_in_days(day1, month1, year1, day2, month2, year2):
    days1 = date_to_days(day1, month1, year1)
    days2 = date_to_days(day2, month2, year2)
    return abs(days2 - days1)

def find_min_sum_position(numbers, current_pos, min_pos, min_sum):
    if current_pos > 90:
        return min_pos
    current_sum = sum(numbers[current_pos:current_pos + 10])
    if current_sum < min_sum:
        min_sum = current_sum
        min_pos = current_pos
    return find_min_sum_position(numbers, current_pos + 1, min_pos, min_sum)


print("Завдання 1")
number = int(input("Введіть число: "))
degree = int(input("Введіть степінь: "))
print(f"{number} в степені {degree} = {power(number, degree)}")

print("\nЗавдання 2")
print("Введіть першу дату:")
day1 = int(input("  День: "))
month1 = int(input("  Місяць: "))
year1 = int(input("  Рік: "))
print("Введіть другу дату:")
day2 = int(input("  День: "))
month2 = int(input("  Місяць: "))
year2 = int(input("  Рік: "))
result = difference_in_days(day1, month1, year1, day2, month2, year2)
print(f"Різниця між датами: {result} днів")
print(f"Рік {year1} переступний? {is_leap_year(year1)}")
print(f"Рік {year2} переступний? {is_leap_year(year2)}")

print("\nЗавдання 3")
numbers = [random.randint(-100, 100) for i in range(100)]
print("Згенерований список з 100 чисел:")
print(numbers)
first_sum = sum(numbers[0:10])
position = find_min_sum_position(numbers, 0, 0, first_sum)
print(f"\nПозиція з мінімальною сумою 10 чисел: {position}")
print(f"Числа з цієї позиції: {numbers[position:position + 10]}")
print(f"Їх сума: {sum(numbers[position:position + 10])}")