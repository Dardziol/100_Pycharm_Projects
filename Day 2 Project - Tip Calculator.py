#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

bill = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip1 = tip / 100
bill_and_tip = bill * tip1
bill_total = bill_and_tip + bill
bill_divided = bill_total / people
bill_divided = round(bill_divided, 2)
bill_divided= "{:.2f}".format(bill_divided)
print(f"Each person should pay: ${bill_divided}")