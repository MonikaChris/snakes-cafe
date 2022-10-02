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
        'Pie': 10,
    },
    'Drinks': {
        'Coffee': 10,
        'Tea': 10,
        'Unicorn Tears': 10,
    }
}


# Calculates number of spaces needed and returns formatted line
def format_line(text):
    space = (width - len(text) - len(margin))

    if space % 2 == 0:
        return margin + ' ' * (space // 2 - offset) + text + ' ' * (space // 2 - offset) + margin
    else:
        return margin + ' ' * (space // 2 - offset) + text + ' ' * (space // 2 + 1 - offset) + margin


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

while running:
    inp = input()

    if inp == 'quit':
        print('Come again soon!')
        running = False

