# 6. Write a python program to check whether a given string is a multiword string or single
# word string using match case statement

s= input("Enter a string")
match s:
    case s if '' in s:
        print("multiword string")
    case s if '' not in s:
        print("single word string")