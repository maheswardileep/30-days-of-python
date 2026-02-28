def add_two_numbers(a,b):
    return a + b
def area_of_circle(r):
    return (r ** 2) * 3.14
total = 0
def add_all_numbers(*n):
    total = 0
    for numbers in n:
        total += numbers
    return total
print(add_all_numbers(2, 2, 224, 23891))
def celsius_to_f(c):
   z = c * 1.8
   y = z + 32
   return y

print(celsius_to_f(23))

def check_season(month):
    if month == "February" or month == "January" or month == "December":
        return "winter"
    elif month == "March" or month == "April" or month == "May":
        return "spring"
    elif month == "June" or month == "July" or month == "August":
        return "summer"
    else:
        return "autumn"

def calculate_slope(first_y, second_y, first_x, second_x):
    (second_x - first_x) / (second_y - first_y)

def slope(y, m, b):
    slope = m
    return slope

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

def capitalize_list_items(lst):
    new = []
    for item in lst:
        upper_case = item.upper()
        new.append(upper_case)
    return new
print(capitalize_list_items(['Apples', 'Bananas', 'Mango']))