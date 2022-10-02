width = 38
offset = 2
greetings = ['Welcome to the Snakes Cafe!', 'Please see our menu blow.', '', 'To quit, at any time, type "quit"']
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

print('*' * width)
for greeting in greetings:
    space = (width - len(greeting))

    if space % 2 == 0:
        print('**' + ' ' * (space//2 - offset) + greeting + ' ' * (space//2 - offset) + '**')
    else:
        print('**' + ' ' * (space//2 - offset) + greeting + ' ' * (space//2 + 1 - offset) + '**')



