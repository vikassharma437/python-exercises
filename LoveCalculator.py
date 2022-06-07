print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_lower_string = name1.lower() + name2.lower()
t = name_lower_string.count("t")
r = name_lower_string.count("r")
u = name_lower_string.count("u")
e = name_lower_string.count("e")
l = name_lower_string.count("l")
o = name_lower_string.count("o")
v = name_lower_string.count("v")
e = name_lower_string.count("e")

true_string = t + r + u + e
love_string = l + o + v + e

love_score = int(str(true_string) + str(love_string))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <=50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")