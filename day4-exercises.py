space = ' '
concatenate = "Thirty" + space + "Days" +space + "Of" + space + "Python"
print (concatenate)

concatenate = "Coding" + space + "For" + space + "All"
print (concatenate)

company = "Coding For All"
print (company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company.capitalize())
print(company.swapcase())
print('Coding' in company)
print(company.replace("Coding", "Python"))
replacement = company.replace("Coding", "Python")
print (replacement.replace("All", "Everyone"))
print(company.split())
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))
print(company[0])
print(company[-1])
print(company[10])
Pfe = "Python For All"
Cfa = "Coding For All"
print(company.index("C"))
print(company.index("F"))
new_thing = "Coding For All People"
print(new_thing.rfind("I"))
conjunction = "You cannot end a sentence with a because because because is a conjunction"
first = int(conjunction.index("because"))
last = int(conjunction.rindex(" is"))
print (conjunction[first:last])
print (company.startswith("Coding"))
print (company.endswith("coding"))
spaced = '   Coding For All      '
print(spaced.strip())
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))
print("I am enjoying this challenge \nI just wonder what is next")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelinski")
