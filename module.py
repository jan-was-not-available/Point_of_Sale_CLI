# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.


class PointOfSale:
  def __init__(self):
    self.checkout_total = 0 # This is an example varialbe, remove it or change it as you please.
    Fruits = {"oranges": int(50), "apples": int(50), "bananas": int(50), "avocado": int(50)}
    Vegetables = {"yuca": int(50), "carrots": int(50), "pumpkin": int(50)}
    Drinks = {"Coca-Cola": int(50), "Dr. Pepper": int(50), "Sprite": int(50), "Orange Juice": int(50), "Apple Juice": int(50)}
    FastFood = {"Cheeseburger": int(50), "Chicken Burger": int(50), "Chili Dog": int(50), "Nachos": int(50), "Pizza": int(50)}
    Menu = [Fruits, Vegetables, Drinks, FastFood]
    print("\nInitializing POS system...")
    
    
  def start(self): # This is the function that should be used to start the application.
    print("\nThe app is not complete.")