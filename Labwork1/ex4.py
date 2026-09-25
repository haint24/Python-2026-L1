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

        