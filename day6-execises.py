double = ()
brothers = ('Ronaldo', 'Messi', 'Neymar')
sisters = ('Mia', 'Mithra', 'Mary')
siblings = brothers + sisters
print(len(siblings))
newsiblings = list(siblings)
newsiblings.append("Remya")
newsiblings.append("Dileep")
family_members = tuple(newsiblings)
*siblings_only, mother, father = family_members
fruits = ('Apple', 'Orange', 'Grapes')
vegetables = ('Onion', 'Potato', 'Squash')
animal_products = ('Butter', 'Milk', 'Meat')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_ls = list(food_stuff_tp)
def middle(lst):
    mid = len(lst) // 2

    if len(lst) % 2 == 0:
        return lst[mid-1], list [mid]
    else:
        return lst[mid]
print(middle(food_stuff_ls))
print(food_stuff_ls[0:3])
print(food_stuff_ls[-3:])
del food_stuff_ls
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'Estonia' in nordic_countries
'Iceland' in nordic_countries
