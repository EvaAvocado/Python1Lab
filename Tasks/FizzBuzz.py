# Task 1

isChooseA = False
while not isChooseA:
    a = input("Введите целое число\n")
    try:
        a = int(a)
        isChooseA = True
    except ValueError:
        print("Вы ввели неправильно, введите целое число")

print("| ", end="")

for i in range(1, a + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz | ", end="")
    elif i % 3 == 0:
        print("Fizz | ", end="")
    elif i % 5 == 0:
        print("Buzz | ", end="")
    else:
        print(str(i) + " | ", end="")
