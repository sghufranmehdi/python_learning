#functions : reusbale block of code that performs a specific task

def greet():
    print("Hello, welcome to Python programming!")
    print("Hello again")
    pass #doesnt return anything, just a placeholder for future code

greet()

def check_weather():
    temperature = 30
    if temperature > 25:
        print("It's a hot day")
    else:
        print("It's a cold day")
    
check_weather()

#parameters and arguments
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python programming!") 

greet_user("Alice")

def weather_report(city, temp):
    print(f"The weather in {city} is {temp} degrees Celsius.")

weather_report("New York", 22)
weather_report("Lahore", 29)

# multiple parameters
def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

# Order matters!
calculate_total(100, 0.08, 10)  # $98

# Default parameters
def notify_user(user, message="You have a new notification!", urgency="Normal"):
    print(f"[{urgency}] Notification for {user}: {message}")

# Use defaults
notify_user("Alice")
# Output: [Normal] Notification for Alice: You have a new notification!

# Override default message
notify_user("Bob", "Your order has been shipped!")
# Output: [Normal] Notification for Bob: Your order has been shipped!

# Override both message and urgency
notify_user("Charlie", "Server is down!", "Critical")
# Output: [Critical] Notification for Charlie: Server is down!

# Another example: just override urgency
notify_user("Dana", urgency="High")
# Output: [High] Notification for Dana: You have a new notification!


# Keyword arguments
# Call functions using parameter names for clarity:
def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)

# Function with return def calculate_area(width, height):
def calculate_area(width, height):
    area = width * height
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft

def get_min_max(numbers):
    return min(numbers), max(numbers)

# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)

