# Constants
width = 38
offset = 1
margin = '**'
greetings = ['Welcome to the Snakes Cafe!', 'Please see our menu blow.', '', 'To quit, at any time, type "quit"']
prompt = 'What would you like to order?'
running = True
menu = {
    'Appetizers': {
        'Wings': 10,
        'Cookies': 10,
        'Spring Rolls': 10,
    },
    'Entrees': {
        'Salmon': 10,
        'Steak': 10,
        'Meat Tornado': 10,
        'A Literal Garden': 10,
    },
    'Desserts': {
        'Ice Cream': 10,
        'Cake': 10,
        'Pie': 1,
    },
    'Drinks': {
        'Coffee': 10,
        'Tea': 10,
        'Unicorn Tears': 10,
    }
}

# Helper Functions


# Calculates number of spaces needed and returns formatted line
def format_line(text):
    space = (width - len(text) - len(margin))

    if space % 2 == 0:
        return margin + ' ' * (space // 2 - offset) + text + ' ' * (space // 2 - offset) + margin
    else:
        return margin + ' ' * (space // 2 - offset) + text + ' ' * (space // 2 + 1 - offset) + margin


# First letter uppercase, other letters lowercase
def cap_first_letters(text):
    line = text
    for idx, letter in enumerate(inp):
        if letter == ' ':
            line = line[:idx + 1] + (line[idx + 1].upper()) + line[idx + 2:]
    return line[0].upper() + line[1:]



# Initialize Cafe

# Print Greeting
print('*' * width)
for greeting in greetings:
    print(format_line(greeting))

# Print Menu
print()
for key in menu.keys():
    print(key)
    print('_' * len(key))
    for item in menu[key]:
        print(item)
    print()

# Print Prompt
print('*' * width)
print(format_line(prompt))
print('*' * width)

# Customer's order
order = {}

# Run cafe
while running:
    inp = input('> ')

    if inp == 'quit':
        if len(order.keys()) == 0:
            print('Come again soon!')
            running = False
        else:
            print('Your order has been processed:')
            for item in order.items():
                print(item)
            print('Come again soon!')
        break

    # Match dictionary capitalization:
    query = cap_first_letters(inp)

    # Check menu and add to order
    found = False
    for foods in menu.values():
        if query in foods:
            if foods[query] > 0:
                foods[query] -= 1
                num_ordered = order.setdefault(query, 0)
                order[query] += 1
                if num_ordered + 1 == 1:
                    print(f'1 order of {query} has been added to your meal.')
                else:
                    print(f'{num_ordered+1} orders of {query} have been added to your meal.')
                found = True
                break
            else:
                print(f'Sorry, we\'re out of {query}. Please make another selection.')
                found = True
                break
    if not found:
        print(f'Sorry, we don\'t have {query}.')
