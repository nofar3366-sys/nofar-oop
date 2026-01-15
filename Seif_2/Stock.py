from Asset import * 

class Stock(Asset):
    
    def __init__(self, Symbol, Current_Price, Quantity , Sector , Dividend):
        super().__init__(Symbol, Current_Price, Quantity)
        self.Sector = Sector
        self.Dividend = Dividend
        
    def calculate_dividend(self):
        Dividend = self._Quantity*self.Dividend
        return Dividend
    
    def __str__(self):
        return f"{super().__str__()}\nType : Stock\nSector : {self.Sector}\nDividend : {self.calculate_dividend()}"
        