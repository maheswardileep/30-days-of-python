# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
len(it_companies)
it_companies.add('Twitter')
it_companies.update('NVIDIA', 'TaTa', 'McKinsey')
it_companies.remove('Facebook')
A.update(B)
A.intersection(B)
A.issubset(B)
A.isdisjoint(B)
A.update(B)
B.update(A)
A.symmetric_difference(B)
del A, B
age_lst = set(age)
len(age)
len(age_lst)
saying = "I am a teacher and I love to inspire and teach people"
split = saying.split(" ")
print(split)
words = set(split)
print(words)

