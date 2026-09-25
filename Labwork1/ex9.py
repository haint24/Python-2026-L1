number = int(input("Enter the number: "))
factorial = 1
if(number == 0):
    print("Factorial of the entered number {} is {}" .format(number, factorial))
else:
    for i in range (1, number + 1):
        factorial = factorial * i
    print("Factorial of the entered number {} is {}" .format(number, factorial))