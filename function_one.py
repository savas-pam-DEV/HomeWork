def show_quote():
    print('"Don\'t let the noise of others\' opinions')
    print('drown out your own inner voice."')
    print('     Steve Jobs')

def show_odd_numbers(a, b):
    for num in range(a, b + 1):
        if num % 2 != 0:
            print(num)

def draw_line(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    elif direction == "vertical":
        for i in range(length):
            print(symbol)

def max_of_four(a, b, c, d):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    if d > maximum:
        maximum = d
    return maximum

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_lucky(number):
    digits = str(number)
    if len(digits) != 6:
        return False
    first_sum = int(digits[0]) + int(digits[1]) + int(digits[2])
    second_sum = int(digits[3]) + int(digits[4]) + int(digits[5])
    return first_sum == second_sum



print("Завдання 1")
show_quote()

print("\nЗавдання 2")
show_odd_numbers(3, 15)

print("\nЗавдання 3")
draw_line(10, "horizontal", "*")

print("\nЗавдання 3")
draw_line(5, "vertical", "#")

print("\nЗавдання 4")
print(max_of_four(3, 17, 8, 5))

print("\nЗавдання 5")
print(is_prime(7))
print(is_prime(10))

print("\nЗавдання 6")
print(is_lucky(123420))
print(is_lucky(723422))