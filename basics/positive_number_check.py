#Exo 1 - Chek if the user input number is positive
number = int(input("Enter the number please: "))

if number > 0 :
    print(f"the number {number} is positive")
elif number < 0 :
    print(f"the number {number} is negative")
else :
    print(f"the number {number} is equal to zero")