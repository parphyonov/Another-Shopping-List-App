import os

shopping_list = []

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clear()
    print(shopping_list)

    new_item = input('What should we add to the shopping list? ').lower()
    if new_item == 'quit':
        break
    else:
        shopping_list.append(new_item)
        continue
