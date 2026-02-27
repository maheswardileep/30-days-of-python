Age = int(input("Enter your age:"))
if Age > 18 or Age == 18:
    print("You are old enough to learn to drive.")
elif Age < 18:
    years_needed = 18 - Age
    print(f"You need {years_needed} more years to learn to drive")

print("Who is older, me or you?")
age = int(input("Enter your age:"))
my_age = 14
if age > my_age:
    greater_than = age - my_age
    print(f"You are {greater_than} years older than me.")
elif age < my_age:
    less_than = my_age - age
    print(f"I am {less_than} years older than you")
else:
    print("You are the same age as me.")

a = input("Enter number one:")
b = input("Enter number two:")
if a > b:
    print(f"{a} is greater than {b}.")
if a < b:
    print(f"{a} is smaller than {b}.")
else:
    print(f"{a} is equal to {b}.")

grade = float(input(("What is your grade right now (100 point scale):")))
if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade <= 79 and grade >= 70:
    print("C")
elif grade <= 69 and grade >= 60:
    print("D")
else:
    print("F")

month = input("What month is it right now (Capitalize first letter):")
if month == "September" or month == 'October' or month == "November":
    print("It is currently Autumn")
elif month == "December" or month == 'January' or month == 'February':
    print ("It is currently winter")
elif month == 'March' or month == 'April' or month == 'May':
    print("It is currently spring")
else:
    print("It is currently summer")

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("What fruit do you want?")
if new_fruit in fruits:
    print ("The fruit already exists in the list")
if new_fruit not in fruits:
    fruits.append(new_fruit)
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    len('skills')  // 2
    print