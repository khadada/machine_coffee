import machine_data


def report(sources=machine_data.machine_resources):
    water = sources['water']
    coffee = sources['coffee']
    milk = sources['milk']
    money = sources['money']
    message_report = f"water: {water}ml \nMilk: {milk}ml \ncoffee: {coffee}g \nmoney: ${money} \n"
    print('='* 90)
    print('this is the report for machine resources'.title())
    print('='* 90)
    print(message_report)
    print('_'* 90)


def purchase(req, resources):
    for ingredient in req :
        remaining = resources[ingredient] - req[ingredient]
        resources[ingredient] = remaining
    print('Take your request. Thank you')


def cappuccino():
    ingredients = machine_data.cappuccino
    print(ingredients)


def espresso():
    ingredients = machine_data.espresso
    print(ingredients)


def latte():
    ingredients = machine_data.latte
    print(ingredients)


machine_operator = {
    'report': report,
    'cappuccino': cappuccino,
    'espresso': espresso,
    'latte': latte
}