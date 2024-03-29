import json
import random





# making a class admin for admin functionality
class Admin_Area:
    def __init__(self):
        # setting attribute a list and file path where information about products stored
         self.product_list=[]               
         self.product_file_path="products/products_details.json"
         self.id_file="products/id_file.txt"   # to store ids


    # mehtod to read data from jsonfile
    def read_from_file(self):
        try:
            with open(self.product_file_path) as file:
                # Try to load data from the file
                data = json.load(file)

            return data    # returning data 
        
        # if file is empty then
        except json.decoder.JSONDecodeError:
            # print("The file is empty or not valid JSON.\n")
            return None


    # to write updated data back to file
    def write_updated_data(self,contents):
        with open(self.product_file_path,"w") as file:
            json.dump(contents,file)

    # making a mehtod to generte random and unique id every time
         
    def assign_id(self):
          with open(self.id_file, "r") as file:
            used_ids = file.read()
            used_ids = used_ids.split("\n")
            while True:
                id = random.randint(1000, 9999)
                if str(id) not in used_ids:
                    used_ids.append(str(id))
                    with open(self.id_file, "a") as file:
                        file.write(f"{id}\n")
                    return id

    def product_name(self):
        contents = self.read_from_file()
        while True:
            product_name = input("Enter Product Name (enter 0 to go back):")

            # If the user wants to go back
            if product_name == "0":
                print("Going back to the previous menu...\n")
                return None  # Return None to indicate going back

            # Check if the product name meets the criteria
            if len(product_name) > 1 and any(char.isalpha() for char in product_name):
                # If products are already present, check if the entered name already exists
                if contents:
                    product_exist = any(check["name"] == product_name for check in contents)
                    if product_exist:
                        print("Product already exists in the Store. Please update its quantity or add another product.\n")
                    else:
                        print("Product name added successfully.\n")
                        return product_name  # Return the product name when added successfully
                else:
                    print("Product name added successfully.\n")
                    return product_name  # Return the product name when added successfully
            else:
                print("Please enter a valid product name with at least one alphabet and more than one character.\n")





    # mehtod to add product company name
                
    def product_company(self):
        while True:
            product_company=input("Enter Product Company name (enter 0 to go back):")

            # if he want to go back
            if product_company=="0":
                print("Going back to previous menu...\n")
                return
            # condition one alphabet and more than one character
            if len (product_company) >1 and any (char.isalpha() for char in product_company):
                print("Product Company Added Successfully\n")
                return product_company
            
            # if not getting valid input
            else:
                print("Please Enter Some thing in product Company Name and atleast one alphabet is required.\n")
    
    # mehtod to take stock input
    
    def quantity_input(self):
        while True:
            try:      # use try except to avoind conflicts
                quantity=int(input("Enter Quantity Of Product (enter 0 to go back):"))
                if quantity==0:    #if he want to go back
                    print("Going back to previous menu..\n")
                    return
                # checking number must be greater than 0
                if quantity>0:
                    print("Quantity of product added successfully.\n")
                    return quantity
                # if quantuty is not valid
                else:
                    print("Please enter non-negative number\n")
            # if not getting input in numbers
            except ValueError:
                print("Please Enter in digits\n")
    

     # mehtod to take price input
    
    def price_input(self):
        while True:
            try:      # use try except to avoind conflicts
                price=int(input("Enter Price Of Product (enter 0 to go back):"))
                if price==0:    #if he want to go back
                    print("Going back to previous menu..\n")
                    return
                # checking number must be greater than 0
                if price>0:
                    print("Price of product added successfully.\n")
                    return price
                # if Price is not valid
                else:
                    print("Please enter non-negative number\n")
            # if not getting input in numbers
            except ValueError:
                print("Please Enter in digits\n")
    

    # making amehtod for process of adding products
    def adding_product_process(self):
        contents=self.read_from_file()
        if not contents:
            contents=[]
        id=self.assign_id()
        if id:
            name=self.product_name()
            if name:
                company=self.product_company()
                if company:
                    quantity=self.quantity_input()
                    if quantity:
                        price=self.price_input()
                        if price:

                            # after getting all input
                            product_dic={"id":id,"name":name,"company":company,"quantity":quantity,"price":price}
                            contents.append(product_dic)
                            # call write data mehtod

                            self.write_updated_data(contents)
                            print("Congratulations Admin Product added successfully.For More Details Visit View products option\n")
    

    # mehtod to show admin all product he added
    def show_products(self):
        contents=self.read_from_file()
        # checking first if no product added yet
        if not contents:
            print("Sportify-Pro is empty this time .No products Details to show..")
            print("Come back later..\n")
            
        else:
            # if something in product list
                    
                        # if something in product list
            print("\t\tSportify-Product Details\n\n")
            print("{:<10} {:<20} {:<20} {:<10} {:<10}".format("Id", "Product-Name", "Company-Name", "Quantity", "Price"))
            print("-" * 80)
            # iterate over 2d data format
            for check in contents:
                print("{:<10} {:<20} {:<20} {:<10} {:<10}".format(check["id"], check["name"], check["company"], check["quantity"], check["price"]))
            print()

    
    # mehtod to remnove any item
            
    def remove_product(self):
        contents = self.read_from_file()
        # checking first if no product added yet
        if not contents:
            print("Sportify-Pro is empty this time. No products details to show.")
            print("Come back later..\n")
            return
        else:
            self.show_products()
            print()
            while True:
                # taking product id input
                try:
                    id_input = int(input("Enter Product Id You Want to delete (enter 0 to go back):"))
                    if id_input == 0:    # if he wants to go back
                        print("Going back to previous option...\n")
                        return

                    # Find the index of the product with the specified ID
                    index_to_remove = None
                    for index, product in enumerate(contents):
                        if product["id"] == id_input:
                            index_to_remove = index
                            break

                    if index_to_remove is not None:
                        # removing that dictionary
                        del contents[index_to_remove]
                        print(f"Item Having id {id_input} is Deleted Successfully.\n")
                        # calling write details to write updated data
                        self.write_updated_data(contents)  # Up
                        return
                    else:
                        print("Invalid Id. No products details Found With That id..\n")
                except ValueError:
                    print("ERROR: Please enter a valid integer.\n")
    

    # mehtod to update product details for admin
    def update_product_details(self):
        # first checking if there are products or not
        contents=self.read_from_file()
        if not contents:
            print("Sportify-pro Is having no stock at this time..You can't Update anything this time..\n")
            print("See You soon...\n")
            return
        else:
            self.show_products()
            print()
            while True:
                # taking product id input
                try:    # use try except to avoid program for crush
                    id_input = int(input("Enter Product Id You Want to delete (enter 0 to go back):"))
                    if id_input == 0:    # if he wants to go back
                        print("Going back to previous option...\n")
                        return
                    
                    # iterate over 2d data format
                    for check in contents:
                        # chjeck if id key value matches with input
                        if check["id"]==id_input:
                            print("Product With that id found .Now What you want you can update for that product..\n")

                            # loop to stuck till he want to back
                            while True:
                                print("1.Update Product Name:")
                                print("2.Update Product Company-Name:")
                                print("3.Update Product Quantity:")
                                print("4.Update Product Price:")
                                print("5.Exit From Update Area:\n\n")
                                # taking choice
                                update_choice=input("Enter your choice what you want to do in update area:")
                                # calling respective mehtods on choices
                                if update_choice=="1":
                                    newname=self.product_name()
                                    if newname:
                                        # change the value
                                        check["name"]=newname
                                        # write updated data
                                        self.write_updated_data(contents)
                                        print("Product Name Update Successfully..\n")
                                        self.show_products()


                                elif update_choice=="2":
                                    newcompany=self.product_company()
                                    if newcompany:
                                        # change the value
                                        check["company"]=newcompany
                                        # write updated data
                                     
                                        self.write_updated_data(contents)
                                        print("Comapny Name Update Successfully..\n")
                                        self.show_products()


                                elif update_choice=="3":
                                    newquantity=self.quantity_input()
                                    if newquantity:
                                         # change the value
                                        check["quantity"]=newquantity

                                        # write updated data
                                        self.write_updated_data(contents)
                                        print("Quantity Update Successfully..\n")
                                        self.show_products()


                                elif update_choice=="4":
                                    newprice=self.price_input()
                                    if newprice:
                                         # change the value
                                        check["price"]=newprice
                                         # write updated data
                                        self.write_updated_data(contents)
                                        print("Price Update Successfully..\n")
                                        self.show_products()


                                elif update_choice=="5":
                                    print("Going back from update area..\n")
                                    return    # if he want to go back
                                # if getting invalid input in choice
                                else:
                                    print("Invalid Update Choice.please Select from given choice\n")
                   # if id not found
                    else:
                        print("Invalid id no id found.\n")
               # if getting input in another form rather tahn digits
                except ValueError:
                    print("ERROR:ID MUST BE IN NUMBERS\n")

                

        
    















 

    # admin login mehtod
    def admin_Login(self):
        admin_username="raza"     # seting admin username and password
        admin_password="123"
        
        while True:
            username=input("\nEnter Admin username (Enter 0 to go back):")
            if username=="0":
                print("Going back to previous menu...\n")
                return
            if username==admin_username:
                print("UserName matches now enter password for further Process\n")
                break
            
            else:
                print("Invalid User-Name Please Enter Valid Credentials.\n")
        
        while True:
                password=input("\nEnter Admin Password (Enter 0 to go back):")
                if password=="0":
                    print("Going back to previous menu...\n")
                    return
                if password==admin_password:
                    print("Wait while we checking Crdentials...\n")
                    print("Congratulations Login Successfull")

                    return password
                
                else:
                    print("Invalid Password Please Enter Valid Credentials.\n")
            
    

    
    # making main page of admin     
    def main_page_Admin(self):
        # calling login function
        admin_login=self.admin_Login()
        # checking if login successfull then call main page
        if admin_login: 
             
            # display options to admin
            print("\t\tWelcome To Admininstration Portal\n")
            while True:
                print("\t1.View all products that Are on Store.")
                print("\t2.Add some products In Store.")
                print("\t3.Remove Products From Store.")
                print("\t4.Update Product Informations/Details.")
                print("\t5.Exit from Administrtaion Portal\n")

                # taking admin choice
                admin_choice=input("Please Admin Enter Your Choice:").strip()

                # now accpording to choices calling the functios
                if admin_choice=="1":
                    self.show_products()
                elif admin_choice=="2":
                    self.adding_product_process()
                elif admin_choice=="3":
                    self.remove_product()
                elif admin_choice=="4":
                    self.update_product_details()
                elif admin_choice=="5":
                    print("Admin portal is ending now...\n")
                    print("Good Bye!!\n")
                    return
                else:
                    print("Invalid choice.Please Enter Valid Choice.\n")


            

                        