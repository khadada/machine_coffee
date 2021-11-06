import machine_data

def report(sources=machine_data.machine_resources):
    water = sources['water']
    coffee = sources['coffee']
    milk = sources['milk']
    money = sources['money']
    message_report = f"water: {water}ml \nMilk: {milk}ml \ncoffee: {coffee}g \nmoney: ${money} \n"
    print('=' * 90)
    print('this is the report for machine resources'.title())
    print('=' * 90)
    print(message_report)
    print('_' * 90)


def get_money():
    quarters = int(input('How many quarter do you have ')) * 0.25
    dimes = int(input('How many dimes do you have ')) * 0.1
    nikcel = int(input('How many nikcel do you have ')) * 0.05
    pinnies = int(input('How many pinnies do you have ')) * 0.01
    total_amount = round(quarters + dimes + nikcel + pinnies,2)
    machine_data.machine_resources['money'] += total_amount
    print(f"Your credit is: ${total_amount}")




def purchase(req, resources=machine_data.machine_resources):
    for ingredient in req:
        remaining = round(resources[ingredient] - req[ingredient],2)
        resources[ingredient] = remaining
    print('Take your request. Thank you')


def cappuccino():
    ingredients = machine_data.cappuccino
    get_money()
    if check_resource(ingredients):
        purchase(ingredients)


def espresso():
    ingredients = machine_data.espresso
    get_money()
    if check_resource(ingredients):
        purchase(ingredients)



def latte():
    ingredients = machine_data.latte
    get_money()
    if check_resource(ingredients):
        purchase(ingredients)


def check_resource(req, resource=machine_data.machine_resources):
    hacker = []
    for ingredient in req:
        if req[ingredient] > resource[ingredient]:
            hacker.append(ingredient)
    if len(hacker) > 0:
        for ingredient in hacker:
            print(f"insufficient resource for {ingredient}")
        return False
    else:
        print('All resources is : OK')
        return True


machine_operator = {
    'report': report,
    'cappuccino': cappuccino,
    'espresso': espresso,
    'latte': latte,
}