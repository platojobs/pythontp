
def make_pizza_test(size,*toppings):
    print(f'\n Making  {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')
