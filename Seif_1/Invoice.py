class Invoice:
    
    def __init__(self , inovice_id , customer_name , date , base_amount , discount):
        self.invoice_id = inovice_id
        self.customer_name = customer_name
        self.date = date
        
        self.is_paid = False
        
        self._discount = discount
        self._base_amount = base_amount
        
    @property
    def base_amount(self):
        return self._base_amount 
        
    @base_amount.setter
    def base_amount(self, value):
        if value < 0 :
            raise ValueError('Base Amount cant be Negative')
        self._base_amount = value
    
    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self , value):
        if value < 0 :
            raise ValueError('Discount cant be Negative')
        
        if self._base_amount < value :
            raise ValueError('Discount cant be Bigger than the Base Amount')
        self._discount = value
        
    def calculate_total(self):
        total_amount = self._base_amount - self._discount
        return total_amount
        
    def mark_as_paid(self):
        self.is_paid = True
        print(f"Invoice : {self.invoice_id} PAID")
        
    def __str__(self):
        status = 'PAID'
        if self.is_paid == False :
            status = 'UNPAID'
        return (f'-----Invoice Number : {self.invoice_id}-----\nCustomer Name: {self.customer_name}\nDate : {self.date}\nBase Amount : {self.base_amount} NIS\nDiscount : {self.discount} NIS\nTotal Amount : {self.calculate_total()} NIS\nStatus : {status}\n')
        
        
            
        
    
        
        
    

  
    
        
    
                
        