from person import *
from model import * 

class view:
    def get_user_input(self):
        print("\n--- Enter Person Details ---")
        name = input('Enter Full Name : ')
        address = input('Enter address : ')
        phone = input('Enter phone : ')
        return name, address, phone
    
    def show_people_list(self, people_list):
        print("\n--- Current People List ---")
        if not people_list:
            print("The list is empty.")
        else:
            for person in people_list:
                print(person)
                
    def display_menu(self):
        print("\n--- Menu ---")
        print("1. Add Person")
        print("2. Show All People")
        print("3. Exit (-1)")
        return input("Choose an option: ")
    
    def display_message(self, message):
        print(f" >> {message}")

    
    
    
