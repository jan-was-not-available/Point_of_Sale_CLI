# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.


class PointOfSale:
  def __init__(self):
    float(self.checkout_total) == 0 # This is an example varialbe, remove it or change it as you please.
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
        print("Fruits: ", self.Fruits)
        print("Vegetables: ", self.Vegetables)
        print("Drinks: ", self.Drinks)
        print("Fast Food: ", self.FastFood)
        self.itemchoice == input("Type Items Here: ")
        if self.itemchoice == ("oranges"):
          float(self.checkout_total) == float(self.checkout_total) + float(1.50)
        if self.itemchoice == ("apples"):
          float(self.checkout_total) == float(self.checkout_total) + float(1.75)
        if self.itemchoice == ("banana"):
          float(self.checkout_total) == float(self.checkout_total) + float(1.25)
        if self.itemchoice == ("avocado"):
          float(self.checkout_total) == float(self.checkout_total) + float(2.50)
        if self.itemchoice == ("yuca"):
          float(self.checkout_total) == float(self.checkout_total) + float(2.20)
        if self.itemchoice == ("carrots"):
          float(self.checkout_total) == float(self.checkout_total) + float(0.50)
        if self.itemchoice == ("pumpkins"):
          float(self.checkout_total) == float(self.checkout_total) + float(3.50)
        if self.itemchoice == ("spinach"):
          float(self.checkout_total) == float(self.checkout_total) + float(0.75)
        


      elif choice == "3":
        print("This is your checkout total: ")
        print("\n=============================")
        print("\n")
        return self.checkout_total 
      

      break