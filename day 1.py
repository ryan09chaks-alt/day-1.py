#Ryan Chakraborty
#Period 2

# Write a function that traverses a list and returns a random name from said list
# Bonus if you write in nested loops for traversal, concatenation of results, etc.

# Including the random module into our program by importing it
import random

# Sets up list of players using strings which random module will select from
lakers = ["Lebron James", "Luka Doncic","Bronny James", "Austin Reaves", "Carmelo Anthony", "Anthony Davis", "Dwight Howard", "Russell Westbrook" ]

# Selects the random player which will be selected from "lakers"
random_player = random.choice(lakers)

# Prints out the random choice from the sports team
print(random_player)


