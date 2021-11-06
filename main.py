from machine_data import *
from fonctionality import *
off = False
while not off:
    user_request = input('What you need? [cappuccino] [espresso] [latte] ')
    if user_request == 'off':
        off = True
    else:
        machine_operator[user_request]()
        print(machine_resources)
