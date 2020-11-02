# Intro to Programming Using Python - Assignment #1
# Completed by: Nailah Akbar
import numpy

# 1. Print out the following text: 
# You've reached [your name]. 
# I'm not available right now, so leave a message and I'll call you back.
answering_message = ("You've reached Nailah Akbar. \nI'm not available right now, so leave a message and I'll call you back.")
print(answering_message)
print()
# I created a variable to include text and used the next line character to separate into two lines.
# I printed the variable.

# 2. Create five variables for your first name, last name, shoe size, height, and age. 
# And then print them out on one line.
first_name = 'Nailah'
last_name =  'Akbar'
shoe_size = '8.5'
height = "5'6"
age = '38'
print(first_name + " " + last_name + " " + shoe_size + " " + height + " " + age)
# another way: vitals = f"{first_name} {last_name} {shoe_size} {height} {age}"
# print(vitals)
# COMMENTS: I created 5 variables for first 
# I set values as my own answers.
# I printed them out on one line.

print()
# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount
# in a variable named total and print it out.
subtotal = 10.58
tip = 0.22
total = (subtotal) * (tip) + (subtotal)
print(total)
print()
# COMMENTS: I created the variables for subtotal, tip and total.
# I created the total variable to include a formula in the value so to calculate total bill cost.

# 4. Convert 158.8 into an integer. 
print(int(158.8))
# COMMENTS: I used the int function to convert the float to an integer.

# Convert 75 into a float. 
print(float(75))
# COMMENTS: I converted the integer to a float using float function.

# Convert "244.9" into a float and then an integer.
print(float("244.9"))
print(int(float("244.9")))
print()
# COMMENTS: I converted the string to a float using float function.
# I nested the float function into the int function from convert string to integer.

# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:
# -in the woods
#               which
#                   stutter
#                           and
# 
#                               sing
print(" -in the woods\n\t\twhich\n\t\t\tstutter \n\t\t\t\tand \n\n\t\t\t\t\tsing")  
print()
# COMMENTS: I used the tab and new line characters to set the lyrics as similarly as I could to the example.
# I printed the string and added a print function for an empty line to space out answers.

# 6. Put your first name and total from above into an f-string (f"...") so that it reads: 
# Mattan, your total is $12.91 
# (remember to round the total to the nearest cent)
print(f"{(first_name)}, your total is ${round(total, 2)}")
# COMMENTS: I used the previously defined variable for my first name 
# I used my first_name variable in an f string that includes the rounding function to round answer.
# I set round function to 2 places so the answer is rounded to the nearest cent.

# 7. Use input() to ask a user for the city they live in, and then print it back to them.
user_City = input('What city do you live in?: ')
print(user_City) 
# COMMENTS: I created a variable and used the input function to include an open ended question 
# I printed variable for user's input/answer

# 8. Build a future value calculator by using input() to get values from the user. 
# (Make sure you convert them into integers or floats before doing any math on them.) 
# Print out the result.
# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods
def calculator_future_value(p,i,t):
	return p * (( 1 + i / 100) ** t)
p = float(input("Enter Present value of the account: "))
i = float(input("Enter monthly deposit" + "interest rate: "))
t = int(input("Enter number of month: "))
f =calculator_future_value(p,i,t)
print("Account's future value is: ",'$' + format( f, '.2f'))
input('Press ENTER to exit')
# COMMENTS: I created variables for present value, interest Rate, length of time,and future value calculater
# I used input function for the values and calculation.
# I printed a statement that included the formula to acheive the future value user seeks.