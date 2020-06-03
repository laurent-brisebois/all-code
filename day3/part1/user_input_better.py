import time

# --------------------
# 1.0 simple example
# --------------------

name = input("Please enter your name: ")
print("Hello,", name, "!")

# cooler
# age = input("Please enter your age: ")
# time.sleep(1)
# print("\nYou're...")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print("Old!")
# time.sleep(1)

# --------------------
# 1.1 using if/else (simple)
# --------------------

kids = input("How many kids do you have? ")
kids_integer = int(kids)

if kids_integer > 0:
    print("Wow that's enough!")
else:
    print("Well get going then!")


# --------------------
# 1.2 check on user input
# --------------------

ice_creams = input("How many ice cream cones can you eat in one sitting? ")

# if the ice_creams variable is a positive integer, follow through
if ice_creams.isdigit() == True:

    ice_creams_integer = int(ice_creams)
    if ice_creams_integer > 7:
        print("Good by me.")
    elif ice_creams_integer > 0 and ice_creams_integer <= 7:
        print("You need to work on that")
    else:
        print("Get out of my class.")

else:
    ice_creams = input(
        "Punk you didn't provide a valid number. I'm asking... how many ice cream cones can you eat in one sitting? ")
