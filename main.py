# IMPORTING ALL CLASSES FROM RESPECTIVE FILES
from register_class import Registration
from login_class import Login
from admin_class import Admin_Area
from user_class import Customers                  




# making instance of classes
registration=Registration()
login=Login()
admin=Admin_Area()
users=Customers()



# main page function

def main_Page():
    print('\n\t"Welcome To Sportify-pro"')
    print("\tOnce You Login you would able to enter in sportify-pro")
    print("------------------------------------------------")
    while True:
        # display options
        print("\t1.Register as customer.")
        print("\t2.Login as customer.")
        print("\t3.Login as Administration.")
        print("\t4.Exit:Top exit from sportify-pro.\n\n")

        # getting user choice
        get_choice=input("Enter Your Choice in sportify-pro:").strip()

        # managing choices

        if get_choice=="1":
            print("\tWelcome To Registration Area")
            registration.registration_process()

        elif get_choice=="2":
            print("\tWelcome To Login Area")
            users.main_page_customers()

        elif get_choice=="3":
            print("Welcome To Administartion Dashboard.")
            admin.main_page_Admin()

        elif get_choice=="4":
            print("Sportify-pro is exiting now.See you soon...\n")
            print("Good Bye!!")
            return    

        else:
            print("\nInvalid Choice.Please select from given choices.\n")

main_Page()


















