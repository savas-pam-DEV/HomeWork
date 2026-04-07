def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def sum_of_digits(number):
    number = abs(number)
    if number < 10:
        return number
    return number % 10 + sum_of_digits(number // 10)

def is_symmetric(lst):
    if len(lst) <= 1:
        return True
    if lst[0] != lst[-1]:
        return False
    return is_symmetric(lst[1:-1])


print("Завдання 1")
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
print(f"Найбільший спільний дільник: {gcd(a, b)}")

print("\nЗавдання 2")
number = int(input("Введіть число: "))
print(f"Сума цифр: {sum_of_digits(number)}")

print("\nЗавдання 3")
user_input = input("Введіть елементи списку через кому: ")
lst = [int(x) for x in user_input.split(",")]
if is_symmetric(lst):
    print("Список симетричний")
else:
    print("Список не симетричний")