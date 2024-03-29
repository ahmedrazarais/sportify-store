
import json     # import json 

# making class for registration process

class Registration:
    def __init__(self):
        # making json file path and an empty array as attrtibutes
        self.json_file_path="accounts/accounts_details.json"
    

    
    # making a mehtod to read data from json file
        
    def read_data_from_file(self):
        try:
            with open(self.json_file_path) as file:
                # Try to load data from the file
                data = json.load(file)

            return data    # returning data 
        
        # if file is empty then
        except json.decoder.JSONDecodeError:
            # print("The file is empty or not valid JSON.\n")
            return None
        
    

    # mehtod to write data
        
    def write_data_to_file(self,account_list):
        with open(self.json_file_path,"w") as file:
            json.dump(account_list,file)

    
    #  mehtod to take username input
            
    def get_username(self):
        contents = self.read_data_from_file()

        while True:
            username = input("Enter username for registration (enter 0 to go back): ")
            username_lower = username.strip().lower()  # Convert to lowercase and remove leading/trailing spaces
            
            if username_lower == "0":
                print("Going back to previous menu...")
                return None
            
            if not username:
                print("Username cannot be empty.")
                continue
            
            if contents is None:
                # File is empty or doesn't exist
                print("No existing accounts found. Username is available.")
                print("Now proceed to enter password....")
                return username_lower
            
            # Check if username already exists
            username_exist = any(check["username"] == username_lower for check in contents)
            
            if not username_exist:
                print("Username is available. Now proceed to enter password....\n")
                return username_lower
            else:
                print("Sorry, this username is already taken. Please choose another one or login.\n")


    # mehtoid to take password input
    def get_password(self):
        while True:
            password=input("Enter Strong Password For Registration (enter 0 to go back):")
            if password=="0":
                print("Going back To previous menu...\n")
                return
            # conditions for password.
            if len(password)>=6 and any(char.isalpha() for char in password) and any(char.isdigit() for char in password ):
                print("Password Set successfully\n")
                return password    # if condition met then return the password 
            else:
                print("\nPassword must contain atleast 6 characters with mix of digitis alphabets.\n")
  
   
    # mehtod to take security answer input
    def security_question(self):
        while True:

            secutity_answer=input("What is favourite Food (enter 0 to back):")
            # if he want to go back
            if secutity_answer=="0":
                print("Going back To previous menu...\n")
                return
            # checking must be something in input
            if len(secutity_answer)<1:
                print("Answer is mandatory for security purpose:\n")
            else:
                return secutity_answer
    
    # registration process
    def registration_process(self):
        data=self.read_data_from_file()
        account_list = data if data else []  # 
        username=self.get_username()
        if username:
            password=self.get_password()
            if password:
                security_answer=self.security_question()
                if security_answer:
                    # making the dictionary
                    data={"username":username,"password":password,"securityanswer":security_answer}
                    # appending data in main list
                    account_list.append(data)
                    #call write data mehtod
                    self.write_data_to_file(account_list)
                    # account created succesffuly
                    print("Congratulations Account Created Successfully.\n")