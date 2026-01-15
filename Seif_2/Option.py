from Asset import * 

class Option(Asset):
    
    def __init__(self, Symbol, Current_Price, Quantity  , Strike_Price , Type , Expiration_Date ):
        super().__init__(Symbol, Current_Price, Quantity)
        self.Strike_Price = Strike_Price
        self.Type = Type
        self.Expiration_Date = Expiration_Date
        
    def is_in_the_money(self):
        if self.Type == "Call":
            return self.Current_Price > self.Strike_Price
        else: 
            return self.Current_Price < self.Strike_Price
            
    def __str__(self):
        return f"{super().__str__()}\nType : Option\nStrike Price : {self.Strike_Price}\n Option Type : {self.Type}\nExpiration Date : {self.Expiration_Date}\n{self.is_in_the_money()}"
        
    