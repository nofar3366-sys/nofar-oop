from Asset import *

class Bond(Asset):
    
    def __init__(self, Symbol, Current_Price, Quantity , Rate , Date):
        super().__init__(Symbol, Current_Price, Quantity)
        self.Rate = Rate
        self.Date = Date
        
    def Calculate_Rate(self):
        Asset_Value = self.calculate_Asset_value()
        Rate_Value = Asset_Value*self.Rate
        return Rate_Value
    
    def __str__(self):
        return f'{super().__str__()}\nType : Bond\nRate : {self.Rate}\nRate Value : {self.Calculate_Rate()}\nDate : {self.Date}' 
    
        
        
     