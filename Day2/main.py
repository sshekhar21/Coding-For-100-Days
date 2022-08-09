# Tip Calculator

# initializing empty stings
base_bill = ""
percentage = ""
people = ""

print("Welcome to the tip calculator.")

# base_bill (without_tip)
while True:
    print("What was the total bill?")
    base_bill = input("> $")
    # trying to convert it into float
    try:
        float(base_bill)
        if float(base_bill) < 0:
            print("The bill can't be negative. Please enter a valid amount.")
        else:
            break
    except ValueError:
        print("Please enter a valid amount.")

# calculating the percentage
while True:
    print("What percentage tip would you like to give? 10, 12, or 15?")
    percentage = input("> ")
    # choice for the tip in percentage
    choices_list = ["10", "12", "15"]
    if percentage not in choices_list:
        print("Please enter 10, 12 or 15.")
    else:
        break

# spliting the bill into number of peoples
while True:
    print("How many people to split the bill?")
    people = input("> ")
    if not people.isdigit() or people == "0":
        print("Please enter a valid number of people (1,2,3, etc.)")
    else:
        break

# add the tip to the base_bill
total_bill = float(base_bill) * (1 + int(percentage) / 100)

# rounding it to 2 decimal places
split_bill = round(total_bill / int(people), 2)

# using a uniform message, even if there was just a single person
print(f"Each person should pay: ${split_bill}")
