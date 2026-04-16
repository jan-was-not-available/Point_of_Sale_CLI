# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.


class PointOfSale:
  def __init__(self):
    self.checkout_total = 0 # This is an example varialbe, remove it or change it as you please.
    self.Cart = []
    self.Fruits = ["oranges", "apples", "banana", "avocado"]
    self.Vegetables = ["yuca", "carrots", "pumpkins", "spinach"]
    self.Drinks = ["coke", "dr.pepper", "sprite", "fanta", "apple juice", "orange juice"]
    self.FastFood = ["cheeseburger", "chicken burger", "chili dog", "nachos", "pizza"]
    print("\nInitializing POS system...")
    
    
  def start(self): # This is the function that should be used to start the application.
    print("=======================================")
    print("\nWelcome to Alejandro's Supermarket...")
    print("\n=======================================")
    while len(self.Cart) <= 0:
      print("What would you like to do today?")
      print("\nOptions:")
      print("1 - Show Cart")
      print("2 - Add Item to Cart")
      print("3 - Show Checkout Total")
      print("4 - Finalize Payment")
      print("5 - Exit")
      choice = input("\nEnter Selection: ")
      print("Message: ")
      if choice == "1":
        print(self.Cart)

      elif choice == "2":
        print("What would you like to add?")
        print("Fruits: ", self.Fruits, "Vegetables: ", self.Vegetables, "Drinks: ", self.Drinks, "Fast Food: ", self.FastFood)

      break