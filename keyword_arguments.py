'''
keyword_arguments are used in function while passing the numerical values
so that the code becomes easy in readability
'''

def calc_total_cost(cost_price, shipping, tax ):
    total_cost = cost_price + shipping + tax
    print(total_cost)


calc_total_cost(cost_price=1000, shipping=120, tax=50)