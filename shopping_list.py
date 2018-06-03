import os

shopping_list = [
    'Fur tree',
    'Silver rings',
    'A photo holder for our family photo'
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_list(shopping_list):
    for item in shopping_list:
        print('{}. {}'.format(shopping_list.index(item) + 1, item))

clear()

while True:
    print('')

    command = input('Enter HELP for a quick introduction of the app.\n> ').lower()
    if command== 'done':
        break
    elif command == 'add':
        new_item = input('What do you add to the list? ')
        shopping_list.append(new_item)
        continue
    elif command == 'show':
        print('')
        show_list(shopping_list)
        continue
    elif command == 'help':
        print('Type ADD to add an item to the shopping list.')
        print('Type SHOW to have a look at the full list.')
        print('Type DONE to close the app.')
    else:
        continue
