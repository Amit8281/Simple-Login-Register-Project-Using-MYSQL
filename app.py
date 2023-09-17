import sys
from dbhelper import DBhelper


class Flipkart:
    def __init__(self):
        # Connect to database
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
        1. Enter 1 to register
        2. Enter to login
        3. Anything else to leave                   
        """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name = input("Enter the Name : ")
        email = input("enter the email : ")
        password = input("enter password : ")

        response=self.db.register(name,email,password)

        if response:
            print("Registration susscessful")

        else:
            print("Registration Failed")

        self.menu()

    def login(self):
        email = input("enter the email : ")
        password = input("enter password : ")

        data = self.db.search(email,password)

        if len(data)==0:
            print("Incorrect Email/Password")
            self.login()

        else:
            print("Hellow",data[0][1])

obj = Flipkart()