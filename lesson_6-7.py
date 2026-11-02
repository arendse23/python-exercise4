# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple","banana","mango","pineapple"]

# TODO: Use a for loop to print each fruit in the list

for fruit in fruits:
    print(fruit)

# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1 
count = 5

while count >= 1:
    print(count)
    count -= 1
print("count")

# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1, 11):
    square = i ** 2
    print(f"{i} = {square}")

 # Question 4: Using the random module e.g random.sample or random.choice

# TODO: Import the random module

# TODO: Create a list of colors

colors = ["yellow","blue","red","green","black"]

# TODO: Use a for loop to select and print 3 random colors from the list
import random
colors = ["yellow","blue","red","green","black"]
random_colors = random.sample(colors, 3)
for colors in random_colors:
    print(colors)

    # Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content