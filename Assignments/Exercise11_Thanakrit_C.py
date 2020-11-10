inputNumber = int((input("Input Number : ")))
for k in range(inputNumber):
    print(" " * (inputNumber - k - 1) + ("*" * (2 * k + 1)))