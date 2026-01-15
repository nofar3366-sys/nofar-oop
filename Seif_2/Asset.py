class Asset:
    
    def __init__(self , Symbol , Current_Price , Quantity ):
        self.Symbol = Symbol
        self._Current_Price = Current_Price
        self._Quantity = Quantity
        
    @property
    def Current_Price(self):
        return self._Current_Price
    
    @Current_Price.setter 
    def Current_Price(self , value ):
        if value < 0 :
            raise ValueError ("Price cant be negative")
        self._Current_Price = value
    
    @property
    def Quantity(self):
        return self._Quantity
    
    @Quantity.setter
    def Quantity(self , value ):
        if value < 0 :
            raise ValueError ("Quantity cant be negative")
        self._Quantity = value
        
    def calculate_Asset_value(self):
        value = self._Current_Price*self._Quantity
        return value
    
    def update_price(self , value ):
        if value > self._Current_Price:
            status = "UP"
            self._Current_Price =  value
        elif value < self._Current_Price:
            status = "DOWN"
            self._Current_Price =  value
        else:
            status = "NO CHANGE"
            self._Current_Price =  value
        
        print(f'---UPDATE---\nStatus : {status}\nCurrent Price : {self._Current_Price}')
        
    def __str__(self):
        return (f'-----Assets-----\nSymbol : {self.Symbol}\nAsset Value : {self.calculate_Asset_value()}')
    
    
        
    
        
    
    
    
    
    