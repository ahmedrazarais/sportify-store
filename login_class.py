import os
import json
from register_class import Registration





# making class login thta inherits registration class       
class Login(Registration):
    def __init__(self):
        self.user_cart_file=""
        self.user_history_file=""
        self.product_file_path="products/products_details.json"
        super().__init__()
    
    
    # making this mehtod to use when any user want to uo0date password so updating json file
    def write_data_to_file(self,contents):
        # first open it an empty so make it empty
        with open(self.json_file_path,"w"):
            pass
        # then writting the updated contents in file
        with open(self.json_file_path,"w") as file:
            json.dump(contents,file)
  

    # first checking username input
    def username_check(self):
        # call read data mehtod
        contents=self.read_data_from_file()
        if contents:
            # check if any accoun open yet

            while True:
                username = input("Enter username for login (enter 0 to go back):")
                if username=="0":     # if he want to go back
                    print("Going back to previous menu...\n")
                    return
                
                contents=self.read_data_from_file()
                # Check if username already exists
                username_exist = any(check["username"] == username for check in contents)
                if username_exist:
                    print("Username found in data...Now proceed for poassword\n")
                    return username      # return the username when username found

                # if invalid username
                else:
                    print("Username not found in data.please enter correct credentials.\n")
        # if no accounts open yet
        else:
            print("You are our First Customer on sportify-pro.Register Then came her for login\n")
    


    # making a mehtod for password checking
    def password_check(self,username): 
        contents = self.read_data_from_file()
        while True:
                password = input("Enter password for login (enter 0 to go back): ")
                if password == "0":     # if he want to go back
                    print("Going back to previous menu...\n")
                    return None

                # Check if the entered password matches the stored password corresponding to username
                for check in contents:
                    if check["username"]==username :
                        if check["password"]==password:
                            print("Password matched. Logging in...\n")
                            return password
                else:
                    print("Incorrect password. Please try again.\n")
                    forgot=False          # initial it to false
                    while True:
                        # asking for forgpot password
                        forgot_password=input("Are You Forgot password (Y/N):").strip().lower()

                        # if invalid input
                        if forgot_password not in ["y","n"]:
                            print("Please Enter Appropiate Keyword (y/n)\n")
                        # if he dont want to reset the password
                        elif forgot_password=="n":
                            print("Alright Try Again..\n")
                            break

                        # if he enter yes if he forgot password
                        else:
                            forgot=True
                            break
                # checking if forgot means that if he want to update
                if forgot:
                    # checking for username
                    for check in contents:
                        if check["username"]==username :
                            # asking for security answer input     
                            security_answer=input("\nEnter what is your favourie food:").strip()

                            #checking is security answer matches
                            if  check["securityanswer"]==security_answer:
                                print("Now reset the password.")                          
                                # calling password mehtod from parent class
                                new_password=self.get_password()
                                # checkingif getting something in input
                                if new_password:
                                    # assign new password to that user
                                    check["password"]=new_password

                                    # write updated data back to json file
                                    self.write_data_to_file(contents)
                                
                                print("\nPassword Updated Successfully..\n")
                                return    # after succesfull updation
                            # if invalid security answer
                            else:
                                print(" Invalid Answer Access Denied..\n")


    def login_process(self):
        # calling username method
        username = self.username_check()
        if username:  # checking if getting input

            # calling password method
            password = self.password_check(username)
            # Inside the login_process method of the Login class

            if password:  # checking if getting input
                # Making file of that user in two folders for cart and history
                cart_folder_path = os.path.join("users_cart", f"{username}.json")
                history_folder_path = os.path.join("users_history", f"{username}.json")

               

                try:
                    if not os.path.exists(cart_folder_path):
                       
                        with open(cart_folder_path, "w") as file:
                            pass
                    self.user_cart_file = cart_folder_path
                    

                    if not os.path.exists(history_folder_path):
                      
                        with open(history_folder_path, "w") as file:
                            pass
                    self.user_history_file = history_folder_path
                    

                    print("Just Hold on...We are at our Sportify-pro")
                    print("Welcome to the sportify-pro \n")
                     # Access user files here using self.user_cart_file and self.user_history_file
                    

                    return "login"

                except Exception as e:
                    print(f"Error occurred during file creation: {e}")
