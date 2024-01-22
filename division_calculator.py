try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them!")
print("Enter 'q' to quit")
while True:
    first_number = int(input("Enter first number: "))
    if first_number == 'q':
        break
    second_number = int(input("Enter second number: "))
    if second_number == 'q':
        break
    answer = first_number / second_number
    print(answer)