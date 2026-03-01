#1. . map takes a function and applies the parameters to create a copy of the original. filter takes a function and parameters and removes things that dont fit based on a boolean return. reduce takes a funciton and puts it down to one single number.
#2.  High order function is a function that takes a function as a parameter or returns a function. Closure is a way of passing on variables after the function has been carried out. A decorator is something that adds functionality without modifying the existing object.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

result = list(map(lambda c: c.upper(), countries))
print(result)

result = list(map(lambda c: c ** 2, numbers))
print(result)

result = list(map(lambda c: c.upper(), names))
print(result)

def land_countries(country):
    if 'land' in country:
        return True
    return False

result = filter(land_countries, countries)
print(list(result))

def six_country(country):
    if len(country) == 6:
        return True
    return False

result = filter(six_country, countries)
print(list(result))

def six_or_more(country):
    if len(country) >= 6:
        return True
    return False

result = filter(six_or_more, countries)
print(list(result))

def e_starters(country):
    if country[0] == 'E':
        return True
    return False

result = filter(e_starters, countries)
print(list(result))


def get_string_lists(list):
    def true_o_false():
        for item in list:
            if type(item) == str:
                return True
            return False
    filtered = list(filter(true_o_false, list))
    return filtered

print(get_string_lists(['Hi']))
    








    