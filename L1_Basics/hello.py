# import requests

print("Hello World from Python")

""" (Multi-line comments --> explains about why instead of what)
# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200
"""

first_name = "Ghufran"
last_name = "Mehdi"
user_age = 25
temperature = 36.5
is_raining = False
user_name = "ghufranmehdi1"
print("Age: ",user_age, "\nName: " ,first_name+" "+last_name, "\nUsername: ", user_name, "\nTemperature: ", temperature, "\nIs Raining: ", is_raining)

# Boolean
is_Logged_in = True
is_true = True
age = 16
can_vote = age >= 18
print("Can vote: ", can_vote)

# Arthematic Operators (Maths)
x = 10
y = 5
print("Addition: ", x + y)
print("Subtraction: ", x - y)
print("Multiplication: ", x * y)
print("Division: ", x / y)
print("Floor Division: ", x // y) #Rounds down to the nearest whole number
print("Modulus: ", x % y)
print("Exponentiation: ", x ** y)   

# Comparison operators
print(age == 25)
print(age != 25)
print(age > 18)
print(age < 18)
print(age >= 18)
print(age <= 18)    

# Logical Operators
age = 25
has_license = True

# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False

# Truth Table
# AND: Both must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# OR: At least one must be True  
print(True or False)    # True
print(False or False)   # False

# NOT: Flips the value
print(not True)         # False
print(not False)        # True


# Assignment shortcuts
# Instead of:
score = 0
score = score + 10
print(score)  # 10

# Write:
score += 10
print(score)  # 20

# Works with all operators
x = 10
x += 5    # x is now 15
x *= 2    # x is now 30

# Strings
greeting = "Hello"
first_name = "Ghufran"
last_name = "Mehdi"
full_name = first_name + " " + last_name
print(full_name)

my_long_string = """
This is a long string that spans multiple lines. 
It can contain "quotes" and 'apostrophes' without any issues.
"""
print(my_long_string)

print("apostrophes" in my_long_string)  # Check if substring exists

new_line_string = my_long_string.replace('"quotes"', "'quotes'")
print(new_line_string)

print(greeting + " " + full_name)  # Concatenation

long_dash = "-" * 30
print(long_dash)  # Repetition

print(len(long_dash)) # Length of the string

# String Formatting using f-strings
print(f"Age is {user_age} and name is {first_name+' '+last_name} and username is {user_name} and temperature is {temperature} and is_raining is {is_raining}")

print(greeting[0])  # Indexing
print(greeting[1:4])  # Slicing
print(greeting.lower())  # Convert to lowercase
print(greeting.upper())  # Convert to uppercase 
print(greeting.title())  # Capitalizes first letter of each word
print(greeting.replace("o", "0"))  # Replace characters
print(greeting.split("e"))  # Split string into a list
print("   Hello World   ".strip())  # Remove whitespace from both ends
print("   Hello World   ".lstrip())  # Remove whitespace from the left
print("   Hello World   ".rstrip())  # Remove whitespace from the right
print("Hello World".startswith("Hello"))  # Check if string starts with a substring
print("Hello World".endswith("World"))  # Check if string ends with a substring
print("Hello World".find("o"))  # Find the index of the first occurrence of a substring
print("Hello World".count("o"))  # Count the occurrences of a substring


# Conditional Statements
temperature = 36.5
if temperature > 30:
    print("It's a hot day")
elif temperature > 20: 
    #if no elif then it will check all the conditions and print all the statements that are true
    print("It's a nice day")
else:
    print("It's a cold day")


has_tickets = True
age = 18
if has_tickets:
    if(age >= 18):
        print("You can watch the movie")
    else:
        print("You are too young to watch the movie")
else:
    print("You need to buy tickets to watch the movie")

# Loops
for i in range(10):
    print(i)

for i in range(1, 11): # range(start, stop) --> start is inclusive and stop is exclusive
    print(i)

for i in range(0, 11, 2): # range(start, stop, step) --> step is the increment value
    print(i)

name = "Python"
for letter in name:
    print(letter)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}")

count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1  # Increase count by 1
    
""" Data Structures in Python:
Lists: Like a shopping list (ordered items)
Dictionaries: Like a phone book (name > number)
Tuples: Like coordinates (fixed values)
Sets: Like a bag of unique items
"""
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

has_license = True
my_list2 = ["Ghufran", 25, True, 36.5, has_license]
print(my_list2[0])
has_license = my_list2[-1]
print(has_license)
my_list2[0] = "Mehdi"
print(my_list2)

my_list2.append("Ghufran Mehdi")
print(my_list2)
my_list2.insert(1, "New Value at Index 1")
print(my_list2)

my_list2.remove(25)
print(my_list2)


my_dict = {
    "name": "Ghufran", 
    "age": 25, 
    "city": "Karachi"
    }
print(my_dict)

scores = dict(math=95, english=87, science=92)
print(scores)