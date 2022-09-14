# 2. Write a menu driven program to perform following operations - Addition, Subtraction,
# Multiplication, Division

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("Enter your choice:")

choice= int(input())

match choice:
    case 1:
        print("Enter two numbers:")
        a,b=int(input()),int(input())
        c=a+b
        print("sum is ",c)
    case 2:
        print("Enter two numbers:")
        a,b=int(input()),int(input())
        c=a-b
        print("Subtraction is ",c)
    case 3:
        print("Enter two numbers:")
        a,b=int(input()),int(input())
        c=a*b
        print("Multiplication is ",c)
    case 4:
        print("Enter two numbers:")
        a,b=int(input()),int(input())
        c=a/b
        print("Division is ",c)
    case _:
        print("Invalid choice")
        