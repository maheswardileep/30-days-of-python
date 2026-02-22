thing = []
veggies = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Asparagus']
print(len(veggies))
print(veggies[0])
middle = len(veggies)//2
print(veggies[middle])
last = len(veggies) - 1
print(veggies[last])
mixed_data_types = ['Mahe', 14, 5.75, False, '12345 Silly Street']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple','IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
middle = len(it_companies) // 2
print(it_companies[middle])
last = len(it_companies) - 1
print(it_companies [last])
it_companies.remove('Facebook')
print(it_companies)
it_companies.append('Nvidia')
it_companies.insert(middle, 'Palantir')
it_companies[2] = 'MICROSOFT'
print('#; '.join(it_companies))
print('Facebook' in it_companies)
it_companies.sort()
it_companies.reverse()
it_companies[0:3]
earlier = len(it_companies) - 4
print(it_companies[earlier:])
it_companies[middle]
it_companies.pop(0)
it_companies.pop(middle)
it_companies.pop()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)