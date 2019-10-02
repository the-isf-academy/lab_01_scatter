# Author: Jacob Wolf
# Pizza data from expandedramblings.com/index.php/the-top-10-most-popular-pizza-toppings-infographic/

def top_toppings():
    """
    Returns a list containing the top 10 pizza toppings according to the link above.
    """
    return([
        "pepperoni",
        "mushrooms",
        "onions",
        "sausage",
        "bacon",
        "extra cheese",
        "black olives",
        "green peppers",
        "pineapple",
        "spinach"
    ])


def topping_rank(topping):
    """
    Returns the ranking of the topping or a string if the topping is not in the
    top ten toppings.
    """
    top_toppings_list = top_toppings()
    topping = topping.lower()
    if not topping in top_toppings_list:
        return "very unique"
    else:
        return top_toppings_list.index(topping)
