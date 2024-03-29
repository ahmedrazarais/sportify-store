import json
import time
from login_class import Login
from admin_class import Admin_Area






# making this class for users/customers inherits witrh both login and admin_area
class Customers(Login, Admin_Area):
    def __init__(self):
        self.cart_list=[]
        super().__init__()

    
   
    
    def update_cart_details(self,cart_list):
        with open(self.user_cart_file,"w") as file:
            json.dump(cart_list,file)


    def read_cart_details(self):
        try:
            with open(self.user_cart_file) as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("Cart file not found.")
        except json.decoder.JSONDecodeError:
            return None

    
    def customer_add_products(self):
        # Read the existing cart details from the file
        data = self.read_cart_details()
        # Initialize cart list with existing data or an empty list
        cart_list = data if data else []
        # Accessing the product list
        contents = self.read_from_file()
        # Check if the product list is empty
        if not contents:
            print("Sportify is empty at this moment. You can't buy anything at this time.\n\n")
        else:
            # Display available products
            self.show_products()
            while True:
                try:
                    # Get the product ID the user wants to purchase
                    id = int(input("Enter Product id you want to purchase (enter 0 to go back): "))
                    if id == 0:
                        # Go back to the previous menu if the user enters 0
                        print("Going back to the previous menu...\n")
                        return
                    product_found = False
                    for product in contents:
                        # Check if the product ID exists in the product list
                        if product["id"] == id:
                            product_found = True
                            if product["quantity"] != 0:
                                # If the product is available, prompt the user to enter the quantity
                                print(f"Product Id Found. Product name is {product['name']}\n\n")
                                while True:
                                    try:
                                        # Get the quantity of the product the user wants to purchase
                                        quantity = int(input(f"Enter Quantity of {product['name']} you want to purchase: "))
                                        if quantity <= product["quantity"]:
                                            # Check if the product is already in the cart
                                            for item in cart_list:
                                                if item["id"] == id:
                                                    # If the product is in the cart, update the quantity and bill
                                                    item["quantity"] += quantity
                                                    item["bill"] += product["price"] * quantity
                                                    print(f"{product['name']} quantity updated to {item['quantity']} in your cart.\n")
                                                    break
                                            else:
                                                # If the product is not in the cart, add it
                                                bill = product["price"] * quantity
                                                details = {
                                                    "id": product["id"],
                                                    "name": product["name"],
                                                    "company": product["company"],
                                                    "quantity": quantity,
                                                    "price": product["price"],
                                                    "bill": bill
                                                }
                                                cart_list.append(details)
                                                print(f"{product['name']} with quantity {quantity} is added to your cart.\n")
                                            # Update product details after purchase
                                            product["quantity"] -= quantity
                                            self.write_updated_data(contents)
                                            # Update cart details
                                            self.update_cart_details(cart_list)
                                            return
                                        else:
                                            print("We don't have enough quantity. Please enter a valid quantity.\n")
                                    except ValueError:
                                        print("Please enter digits for quantity. Non-negative numbers only.\n\n")
                            else:
                                print(f"Product {product['name']} is out of stock now.\n")
                    if not product_found:
                        print("Product id not found. Please enter a valid id.\n")
                except ValueError:
                    print("Please enter digits for product id. Non-negative numbers only.\n\n")




    
    # this mehtod is to show user cart
    def user_cart(self):
        data=self.read_cart_details()       # calling cart details mehtod to access user cart
        if not data:     # checking if cart is empty or not
            print("\nDear Customer Your Cart is empty Nothing to Display...Do some shopping Then Came back\n\n")
        else:
            
                         # if something in product list
            print("\t\tCart--Details\n\n")
            print("{:<15} {:<25} {:<20} {:<15} {:<15} {:<15}".format("Id","Product-Name", "Company-Name", "Quantity", "Product-Price","Total-Bill"))
            print("-" * 110)
            # iterate over 2d data format
            for product in data:
                print("{:<15} {:<25} {:<20} {:<15} {:<15} {:<15}".format(product["id"],product["name"], product["company"], product["quantity"], product["price"], product["bill"]))
            print()
    

    # remove any product from cart
    def remove_products_from_cart(self):
        data=self.read_cart_details()       # calling cart details mehtod to access user cart
        contents=self.read_from_file()    # call this mehtod of mainlist
        if not data:     # checking if cart is empty or not
            print("\nDear Customer Your Cart is empty Nothing to Display...Do some shopping Then Came back.You can't delete anything at this time\n\n")
            return
        else:
            self.user_cart()     #calling to display users cart 
            while True:
                # taking product id input he want to remove
                # taking product id input
                try:
                    id_input = int(input("Enter Product Id You Want to delete (enter 0 to go back):"))
                    if id_input == 0:    # if he wants to go back
                        print("Going back to previous option...\n")
                        return

                    # Find the index of the product with the specified ID
                    index_to_remove = None
                    for index, product in enumerate(data):
                        if product["id"] == id_input:
                            index_to_remove = index
                            break

                    if index_to_remove is not None:
                        # getting quantity from cart of that product
                        quantity=product["quantity"]
                        
                        # update quantity in main product list

                        # removing that dictionary
                        del data[index_to_remove]
                        print(f"Item Having id {id_input} is Deleted Successfully.\n")
                        # calling write details to write updated data
                        self.update_cart_details(data) 
                        for check in contents:  # update in main product lit
                            if check["id"]==id_input:
                                check["quantity"]+=quantity
                                self.write_updated_data(contents)
                        return
                    else:
                        print("Invalid Id. No products details Found With That id..\n")
                except ValueError:
                    print("ERROR: Please enter a valid integer.\n")
    

    # mehtod to read data from history file
    def history_read(self):
        try:
            with open(self.user_history_file) as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("Cart file not found.")
        except json.decoder.JSONDecodeError:
            return None
                    
    # mehtod for checkout
    def checkout(self):
        # Load existing purchase history
        contents = self.history_read()

        # Read the current cart details
        data = self.read_cart_details()
        
        # Check if the cart is empty
        if not data:
            print("\nDear Customer, Your cart is empty. Please add some items to proceed with checkout.\n")
            return

        # Display the cart details
        self.user_cart()

        # Confirm with the user before proceeding with checkout
        while True:
            confirmation = input("Are you sure you want to proceed with checkout? (Y/N): ").lower()
            if confirmation not in ["y", "n"]:
                print("Invalid input. Please enter 'Y' or 'N'.")
            elif confirmation == "n":
                print("Alright, returning to options menu.")
                return
            else:
                # Calculate total bill
                total_bill = sum(item["bill"] for item in data)
                
                # Get the current time
                current_time = time.ctime()

                # Create a new 2D list to represent the shopping session
                shopping_session = []
                for item in data:
                    shopping_session.append({
                        "id": item["id"],
                        "name": item["name"],
                        "quantity": item["quantity"],
                        "price": item["price"],
                        "total": item["bill"]
                    })

                # Append the new shopping session to the purchase history
                if contents:
                    contents.append({"time": current_time, "items": shopping_session, "total_bill": total_bill})
                else:
                    contents = [{"time": current_time, "items": shopping_session, "total_bill": total_bill}]

                # Display the total bill to the user
                print(f"\nYour total bill is: {total_bill} PKR.")
                print("\nThank you for shopping with us!\n")

                # Write the updated purchase history to file
                with open(self.user_history_file, "w") as file:
                    json.dump(contents, file)

                # Clear the user's cart
                with open(self.user_cart_file, "w") as file:
                    pass
                
                exit()

    
    # mehtod to show user his history
    def history(self):
        data=self.history_read()
        
        if not data:
            print("You haven't made any purchases yet.\n\n")
            return   # if no purchases done yet
        else:
            # Iterate over each entry in the purchase history
            for entry in data:
                # Print the time
                print("Time:", entry["time"])
                print("\n")
                # Print the shopping session
                print("Shopping Session:\n")
                for item in entry["items"]:
                    print("-", item["name"], "x", item["quantity"], "at", item["price"], "each")
                # Print the total bill
                print("Total Bill:", entry["total_bill"])
                # Add a separator for better readability
                print("-" * 50)
        
    
    
                        



            
           


                     

        







    
    # main page of customers
    def main_page_customers(self):
        login=self.login_process()     # fisrt taking login credentials
        if login: # if succesfull login then display menu
            print("\t\tWelcome To sportify-Pro\n\n")
            while True:
                # DISPLAY MENU TO USER
                print("\t1.See Sportify-Product List\t\t5.See any offers and discounts.")
                print("\t2.Add Any Product To your Cart.\t\t6.Checkout From Application.")
                print("\t3.View Your cart Details.\t\t7.Remove products From Cart")
                print("\t4.See Your Purchase History.\t\t8.Exit: exit from customers area.")
                print("\n\n\n")

             
                # getting user choice
                user_choice=input("Dear Customer Enter Your Choice:")
                # calling respective mehtods according to choice
                if user_choice=="1":
                    self.show_products()
                elif user_choice=="2":
                   self.customer_add_products()
                elif user_choice=="3":
                    self.user_cart()
                elif user_choice=="4":
                    self.history()
                elif user_choice=="5":
                    print("\ncoming soon...\n\n")
                elif user_choice=="6":
                    self.checkout()
                elif user_choice=="7":
                    self.remove_products_from_cart()
                elif user_choice=="8":
                    print("Sportify-Pro is exiting now...Catch you later")
                    return   # if he want to exit
                else:
                    print("Invalid Choice.Please select from given choice\n\n")





