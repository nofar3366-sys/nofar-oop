from person import * 

class model:
    
    def __init__(self):
        
        self.people = []
        
    def add_person(self, name, address, phone):
        new_person = Person(name, address, phone)
        self.people.append(new_person)
        
    def get_all_people(self):
        return self.people

