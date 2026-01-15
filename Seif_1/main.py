from Invoice import * 

def main():
    Inv_id = input("Enter Invoice ID: ")
    Name = input("Enter Customer Name: ")
    Date = input("Enter Date (dd/mm/yyyy): ")
    Amount = float(input("Enter Base Amount: "))
    Dis = float(input("Enter Discount: "))
    
    My_Invoice = Invoice(Inv_id , Name , Date , Amount , Dis)
    print("\n-----Invoice Created Successfully-----")
    
    final_price = My_Invoice.calculate_total()
    print(f'Total Amount After Discount : {final_price} NIS\n')
    print("\tInvoice Details    ")
    print(f'{My_Invoice}\n')
    
    payment = input('Payment Completed ? (Y/N)')
    if payment.capitalize() == 'Y': 
        My_Invoice.mark_as_paid()
    print(My_Invoice)
    



if __name__ == "__main__":
    main()