# 10. Write a program to display day name on the basis of user’s liking of a colour. Ask
# user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display
# day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday


s1=input("what is your favorite colour:")
l1=["Yellow","Blue","Orange","Black","Red"]

for colour in l1:
    if colour in s1:
        c=colour
        break
    else:
        c="other"
    match c:
        case "Yellow":
            print("Monday")
        case "Blue":
            print("Tuesday")
        case "Orange":
            print("Wednesday")
        case "Black":
            print("Thursday")
        case "Red":
            print("Friday")
        case "other":
            print("Sunday")
    print