import string
import random
def random_id():
    characters = string.ascii_letters + string.digits
    user_id = ' '
    
    for x in range(6):
        user_id += random.choice(characters)
    return user_id
print (random_id())


user_input1 = int(input("How many characters do you want in your user id?"))
user_input2 = int(input("How many IDs do you want to generate?"))

def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits
    ids = []
    for i in range(user_input2):
        user_id = ""
        for x in range(user_input1):
            user_id += (random.choice(characters))
        print (user_id)

print(user_id_gen_by_user())

def rgb_color_generation():
    rgb = []
    for i in range(0,3):
        i = random.randrange(0,256)
        rgb.append(i)
    rgb = tuple(rgb)
    return rgb

print(rgb_color_generation())

def list_of_hexa_colors(desired_length):
    characters = string.ascii_letters[0:6] + string.digits[0:10]
    hexa_colors = []

    for x in range(desired_length):
        y = ""
        for x in range (6):
            x = random.choice(characters)
            y += x
        hexa_colors.append("#" + y)
    return hexa_colors
print(list_of_hexa_colors(5))

def list_of_rgb_colors(desired_length):
    rgb_colors = []
    for x in range(desired_length):
        color = []
        for y in range(3):
            color.append(random.randint(0, 255))
        rgb_colors.append(f"rgb({color[0]},{color[1]},{color[2]})")
    return rgb_colors

print(list_of_rgb_colors(3))

def generate_colors(desired_length, type):
    if type == "rgb":
        rgb_colors = []
        for x in range(desired_length):
            color = []
            for y in range(3):
                color.append(random.randint(0, 255))
            rgb_colors.append(f"rgb({color[0]},{color[1]},{color[2]})")
        return rgb_colors
    
    if type == "hexa":
        characters = string.ascii_letters[0:6] + string.digits[0:10]
        hexa_colors = []
        for x in range(desired_length):
            y = ""
            for x in range (6):
                    x = random.choice(characters)
                    y += x
            hexa_colors.append("#" + y)
        return hexa_colors
        

print(generate_colors (4, "hexa"))

def shuffle_list(lst):
    new_list = list(lst)
    length = len(new_list) - 1
    for x in new_list:
        exclusion = new_list.index(x)
        random.randint

def random_numbers():
    lst = []
    while len(lst) < 7:
        x = random.randint(0, 10)
        if x not in lst:
            lst.append(x)
    return lst


print(random_numbers())