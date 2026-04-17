# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make the Point of Sale Application functional.


class PointOfSale:
  def __init__(self):
    self.checkout_total = 0.0 # This is an example varialbe, remove it or change it as you please.
    self.Cart = []

    self.Fruits = ["oranges", "apples", "banana", "avocado"]
    self.Vegetables = ["yuca", "carrots", "pumpkins", "spinach"]
    self.Drinks = ["coke", "dr.pepper", "sprite", "fanta", "apple juice", "orange juice"]
    self.FastFood = ["cheeseburger", "chicken burger", "chili dog", "nachos", "pizza"]

    print("\nInitializing POS system...")

  def print_receipt(self):
      print("\n========== Receipt ==========")

      if not self.Cart:
          print("No items purchased")
          return
      
      total = 0 

      prices = {
        "oranges": 1.50,
        "apples": 1.75,
        "banana": 1.25,
        "avocado": 2.50,
        "yuca": 2.20,
        "carrots": 0.50,
        "pumpkins": 3.50,
        "spinach": 0.75,
        "coke": 2.00,
        "dr.pepper": 2.15,
        "sprite": 2.20,
        "fanta": 2.05,
        "apple juice": 3.50,
        "orange juice": 3.75,
        "cheeseburger": 4.00,
        "chicken burger": 3.50,
        "chili dog": 2.50,
        "nachos": 7.50,
        "pizza": 12.00
      }
      
      for item in self.Cart:
          price = prices.get(item, 0)
          total += price
          print(f"{item:15} $ {price:.2f}")

      print("-----------------------------")
      print(f"TOTAL:           $ {total:.2f}")
        

    

  def start(self): # This is the function that should be used to start the application.
    print("=======================================")
    print("\nWelcome to Alejandro's Supermarket...")
    print("\n=======================================")

    while True:
      print("\nWhat would you like to do today?")
      print("Options:")
      print("1 - Show Cart")
      print("2 - Add Item to Cart")
      print("3 - Show Checkout Total")
      print("4 - Finalize Payment")
      print("5 - Exit")
      print("6 - Remove Item(s)")

      choice = input("\nEnter Selection: ")

      if choice == "1":
        print("\nCart", self.Cart)

      elif choice == "2":
        print("\nAvailable Items: ")
        print("Fruits: ", self.Fruits)
        print("Vegetables: ", self.Vegetables)
        print("Drinks: ", self.Drinks)
        print("Fast Food: ", self.FastFood)

        itemchoice = input("Type Items Here: ").lower()

        prices = {
          "oranges": 1.50,
          "apples": 1.75,
          "banana": 1.25,
          "avocado": 2.50,
          "yuca": 2.20,
          "carrots": 0.50,
          "pumpkins": 3.50,
          "spinach": 0.75,
          "coke": 2.00,
          "dr.pepper": 2.15,
          "sprite": 2.20,
          "fanta": 2.05,
          "apple juice": 3.50,
          "orange juice": 3.75,
          "cheeseburger": 4.00,
          "chicken burger": 3.50,
          "chili dog": 2.50,
          "nachos": 7.50,
          "pizza": 12.00
        }

        if itemchoice in prices:
          self.Cart.append(itemchoice)
          self.checkout_total += prices[itemchoice]
          print(f"{itemchoice} added to cart")
        else:
          print("Item not recognized :( ")

      elif choice == "3":
        print("\nCheckout Total: $", round(self.checkout_total, 2))

      elif choice == "4":
        self.print_receipt()
        print("Payment complete. Thank You!")
        self.Cart = []
        self.checkout_total = 0.0

      elif choice == "5":
        print("Goodbye! Come again soon!")
        break
      elif choice == "6":
        if not self.Cart:
            print("\nCart is empty. Nothing to remove.")
        else:
            print("\nYour cart:")
            for item in self.Cart:
                print("-", item)
            
            item_to_remove = input("\nType item to remove: ").lower()

            if item_to_remove in self.Cart:
                self.Cart.remove(item_to_remove)

                if item_to_remove in prices:
                    self.checkout_total -= prices[item_to_remove]
                print(f"{item_to_remove} removed from cart.")
            else:
                print("Item not found in cart.")
      else:
        print("Invalid option. Try again")