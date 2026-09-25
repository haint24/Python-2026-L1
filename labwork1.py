# ==================== Exercise 1 ====================
radius = float(input("Enter the radius: "))
pi = 3.1415926
area = pi * radius ** 2
print("The area is: ", area)


# ==================== Exercise 2 ====================
Celsius = float(input("Enter temperature in Celsius: "))
Fahrenheit = (Celsius * 1.8) + 32
print(Celsius, "(C) = ", Fahrenheit, "(F)")


# ==================== Exercise 3 ====================
number = int(input("Enter a number:"))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is a NOT a prime number")
            break
        else:
            print(number, "is a prime number")
            break
else: 
    print(number, "is a NOT a prime number")


# ==================== Exercise 4 ====================
number = int(input("Enter a number:"))
divisor = 0
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            divisor = i + 1
if divisor == number:
    print(number, "is a perfect number")
else:
    print(number, "is NOT a perfect number")


# ==================== Exercise 5 ====================
List_colors = ["red", "green", "blue", "yellow", "purple"]
colors = input("What is your favorite color?")
if colors in List_colors:
    index = List_colors.index(colors)
    print("Your color is at index", index,"in my list")
else:
    print("Sorry, I could not find your color")


# ==================== Exercise 6 ====================
range1 = list(range(0,7))
range2 = list(range(1,10, 3))
range3 = list(range(5, 1, -1))
range4 = list(range(6, -2, -2))
print("Range 1:", range1)   
print("Range 2:", range2)
print("Range 3:", range3)
print("Range 4:", range4)


# ==================== Exercise 7 ====================
def remove_dollar_sign(s):
    return s.replace('$', '')
test_string = "$100"
result = remove_dollar_sign(test_string)
print(result)  


# ==================== Exercise 8 ====================
def extract_even (l):
    even_numbers = []
    for num in l:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
sample_list = [1, 4, 5, -1, 10]
result = extract_even(sample_list)
print(result)


# ==================== Exercise 9 ====================
number = int(input("Enter the number: "))
factorial = 1
if(number == 0):
    print("Factorial of the entered number {} is {}" .format(number, factorial))
else:
    for i in range (1, number + 1):
        factorial = factorial * i
    print("Factorial of the entered number {} is {}" .format(number, factorial))


# ==================== Exercise 10 ====================
number = int(input("Enter a number:"))
for i in range(1, number + 1):
    if (number % i) == 0:
        print(i)
else:
    print("end")


# ==================== Exercise 11 ====================
x1 = float(input("Enter x1 value: "))
x2 = float(input("Enter x2 value: "))
y1 = float(input("Enter y1 value: "))
y2 = float(input("Enter y2 value: "))
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print ("The distance between two points is", distance)


# ==================== Exercise 12 ====================
def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_pattern(4,5)
