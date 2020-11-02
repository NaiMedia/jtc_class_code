# Intro to Programming Using Python - Assignment #2
# Completed by: 

# 1. Write an if statement that checks if user is "mattangriffel"
# and prints out "Welcome professor" if so, or "Who are you?" if not.

user = "mattangriffel"
if user == "mattangriffel":
	print("Welcome professor")

else:
	print("Who are you?")

# comment: create an if statment that checks user response to be correct/incorrect.

# 2. Write an if statement that checks both the credentials below
# and prints "Successfully logged in." if they're correct or
# "Invalid username/password combination. Try again." if they're not.

user = "mattangriffel"
password = "123456"

if user == "mattangriffel" and password == "123456":
	print("Successfully logged in.")

else:
	print("Invalid username/password combination. Try again.")

# comment: created an if statement in order to print responses to either correct/incorrect user info. 

# 3. Write an if statement that checks whether the value of number is divisible
# by two and prints out "even" if it is and "odd" if it's not.
# (Hint: You can check divisiblity using the modulus (%) operator. 
# n % k == 0 evaluates to true if n is an exact multiple of k.)

number = 4

if number % 2 == 0:
	print('even')

else:
	print('odd')

# comment: created an if statment and used a modulus to determine wheter 4 was divisible evenly.

# 4. Create three different lists containing:
# - The names of all your siblings
# - Your top 3 favorite movies
# - The latitude and longitude coordinates of Columbia University
siblings = ['Bigger Bro', 'Big Bro', 'Lil Sis']
favorite_movies = ['Black Panther', 'Hidden Figures','Coming to America']
CU_coordinates = ['40.8075 N', '73.9626 W']

# Comment: Created 3 different lists.

# 5. Use a for loop on each of the lists above to print out each element on its own line.
for sibling in siblings:
	print(*sibling)

for favorite_movie in favorite_movies:
	print(*favorite_movie)

for CU_coordinate in CU_coordinates:
	print(*CU_coordinate) 
print()	

# Comment: used a for loop and printed each element on it's own line.

# 6. Use a for loop and the title() function to print out each city name capitalized

cities = ["new york city", "san francisco", "boston", "chicago", "los angeles"]

for city in cities:
	print(city.title())

# Comment:  Creat a for lood and to Capitalize each city name in the list I used the title functioon.

# 7. A list is different from an element in a list.  What's something you can do
# to the second in Python that you can't do to the first, and vice versa?

# person = ["Mattan"]
# we can
# run many functions on a list
# append
# remove
# iterate through a list


# person = "Mattan"
# use functions such as 
# upper
# lower
# join
# split

# Comment: created a list of a few things that each of the list and the string can do.

# 8. Use range() and a for loop to print out:
# - the numbers from 1 to 10
# - the square of each of the numbers from 1 to 10
# - for each number from 1 to 10, print out whether it is even or not
 
for number in range(10):
	print(number)
	print(number**2)
	if number % 2 == 0:
		print("even")
	else:

		print("odd")

# Comment: create a for loop using the range function.

# # Bonus: In Mathematics, a Marsenne number is a number that is one less than a
# # power of two (i.e. 2^n - 1). Starting with an empty list named 
# # marsenne_numbers (provided for you below),  use the append() function inside
# # of a for loop so that after the loop has run, marsenne_numbers contains a
# # list of the first ten Marsenne numbers.

# marsenne_numbers = []