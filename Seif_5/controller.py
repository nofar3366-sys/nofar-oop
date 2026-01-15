from model import * 
from view import * 
from person import * 

class Controller:
    def __init__(self):
        self.model = model()
        self.view = view()

    def run(self):
        while True:
            choice = self.view.display_menu()

            if choice == "-1":
                self.view.display_message("Exiting the program. Goodbye!")
                break

            elif choice == "1":
                name, address, phone = self.view.get_user_input()
                self.model.add_person(name, address, phone)
                self.view.display_message("Person added successfully!")

            elif choice == "2":
                all_people = self.model.get_all_people()
                self.view.show_people_list(all_people)

            else:
                self.view.display_message("Invalid option, try again.")
    
        
        
    
    