def show_quote():
    print('"Don\'t compare yourself with anyone in this world...')
    print('   if you do so, you are insulting yourself."')
    print('      Bill Gates')

def show_even_numbers(a, b):
    for num in range(a, b + 1):
        if num % 2 == 0:
            print(num)

def draw_square(size, symbol, filled):
    for row in range(size):
        if filled:
            print(symbol * size)
        else:
            if row == 0 or row == size - 1:
                print(symbol * size)
            else:
                print(symbol + " " * (size - 2) + symbol)

def count_digits(number):
    number = abs(number)
    count = len(str(number))
    return count

def is_palindrome(number):
    digits = str(number)
    length = len(digits)
    half = length // 2
    first_part = digits[:half]
    second_part = digits[length - half:]
    return first_part == second_part[::-1]

print("Завдання 1")
show_quote()

print("\nЗавдання 2")
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
show_even_numbers(a, b)

print("\nЗавдання 3")
size = int(input("Введіть довжину сторони квадрата: "))
symbol = input("Введіть символ: ")
filled_input = input("Заповнений квадрат? (True/False): ")
filled = filled_input == "True"
draw_square(size, symbol, filled)

print("\nЗавдання 4")
number = int(input("Введіть число: "))
print("Кількість цифр:", count_digits(number))

print("\nЗавдання 5")
number = int(input("Введіть число: "))
print("Паліндром?", is_palindrome(number))