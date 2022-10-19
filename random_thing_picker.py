import random

print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to Random Thing Picker 1.0
By: Austin Gause
Est. 10/18/2022

Instructions:
~ Enter items seperated by a comma into the terminal next to the '>' symbol.
~ When you have entered all the items you want to be picked from, press enter.
~ The program will do the rest.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

user_items_input = str(input('Enter all items seperated by a comma:\n> '))
user_items_list = []

def input_formatting():
    to_list = user_items_input.split(',')
    for item in to_list:
        user_items_list.append(item.strip())

input_formatting()

final_selection = random.choice(user_items_list)

print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The item chose by the Wise Mystical Old Oak Tree is:
{final_selection.upper()}!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
