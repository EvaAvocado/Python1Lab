# Task 1

isChooseA = False
while not isChooseA:
    a = input("Введите целое число\n")
    try:
        a = int(a)
        isChooseA = True
    except ValueError:
        print("Вы ввели неправильно, введите целое число")

if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
elif a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
    print("Buzz")
else:
    print(a)
