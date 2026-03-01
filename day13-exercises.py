numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [i for i in numbers if i <= 0]
print(negative_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = [number for row in list_of_lists for number in row ]
print(flattened_list)

lst = [(x, x ** 0, x ** 1, x ** 2, x ** 3, x ** 4, x ** 5) for x in range(11)]
print(lst)


countries = [[('Finland', 'Helsinki')],[('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list = []

for country in countries:
    name, capital = country[0]
    new_list.append([
        name.upper(),
        name[:3].upper(),
        capital.upper()
    ])

print(new_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


new_list = [
    {'country': country.upper(), 'city': town.upper()}
    for city in countries
    for country, town in city
]

print(new_list)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
empty_list = []

full_names = [first + ' ' + last for sublist in names for first, last in sublist]
print(full_names)