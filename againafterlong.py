name = "shreyash"
age = 25
height = 5.9
is_developer = True
print(f"Name: {name}, Age: {age}, Height: {height}, Is Developer: {is_developer}")

score = 85

if score > 90:
    print("Grade: A")
elif score > 80:
    print("Grade: B")
else:
    print("Grade: C")
print("Done")

is_admin = True
has_access = False

if is_admin and not has_access:
    print("Granting access...")

status = "ready"
if status == "ready" or status == "go":
    print("Status is either ready or set");

tech_stack = ["Python", "JavaScript", "React","SQL"]

for tool in tech_stack:
    print(f"I am learning {tool}")

for i in range (5):
    print(i)

prices = [10,55,20,80,5]
for i in prices:
    if i > 50:
        print("Too expensive")
    else:
        print("Buying it")

def greet_user(username):
    print(f"Hello, {username}!")
greet_user("Shreyash")

def square(number):
    result = number * number
    return result
x = square(4)
print(x)

def make_coffee(sugar=1, milk=True):
    print(f"Coffee with {sugar} suagar(s). Milk: {milk}")

make_coffee()
make_coffee(3,False)

def check_temperature(temp):
    if temp < 0:
        return "Freezing"
    elif temp >= 0 and temp <= 20:
        return "cold"
    else:
        return "Warm"

print(check_temperature(15))

student = {
    "name" : "shreyash",
    "id": 402,
    "courses": ["math", "science"]
}
print(student["name"])
print(student["courses"])

student["age"] = 25
print(student)

for k in student:
    print(k)

for key, value in student.items():
    print(f"{key}: {value}")

product = {
    "name": "Laptop",
    "price": 1000
}

product["price"] = 900
product["stock"] = 50

print(product)
