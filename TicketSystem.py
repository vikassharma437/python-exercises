print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Please pay ${bill}.")
    elif age >= 12 and age <= 18:
        bill = 7
        print(f"Please pay ${bill}.")
    else:
        bill = 12
        print(f"Please pay ${bill}.")

    want_photo = input("Do you want photo? Y or N ")
    if want_photo == "Y":
        bill += 3
    print(f"Your final bill amount is: ${bill}")	
else:
    print("You need to grow taller to ride the rollercoaster.")