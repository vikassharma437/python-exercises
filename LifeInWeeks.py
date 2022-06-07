age = input("What is your current age?")

if(len(age) == 2):
    if(age.isnumeric()):
        total_age = 90
        years_left = total_age - int(age)
        months_left = years_left * 12
        weeks_left = years_left * 52
        days_left = years_left * 365
        print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
    else:
        print("Age should be in numeric format.")
else:
    print("Please enter the age value in two digits.")



