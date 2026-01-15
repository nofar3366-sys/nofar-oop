from Asset import *
from Stock import * 
from Bond import * 
from Option import * 

def main():
    Sym = input("What is your Asset ? ")
    Curr_Price = float(input("What is the current price ? "))
    Quant = float(input("How many Assets ? "))
    
    print("\n--- Asset ---")
    My_Asset = Asset(Sym , Curr_Price , Quant )
    print(My_Asset)
    print()
    New_Price = float(input("Enter a new price to update: "))
    My_Asset.update_price(New_Price)
    print(My_Asset)
    print()

    print("\n--- Creating Stock ---")
    stock_sector = input("Enter Sector: ")
    stock_div_rate = float(input("Enter Dividend per Share: "))
    
    My_Stock = Stock(Sym, Curr_Price, Quant , stock_sector, stock_div_rate)
    print(My_Stock)
    print()
    New_Price = float(input("Enter a new price to update: "))
    My_Stock.update_price(New_Price)
    print()
    div_income = My_Stock.calculate_dividend()
    print(f"Total Dividend Income: {div_income}")
    print(My_Stock)
    
    print("\n--- Creating Bond ---")
    bond_rate = float(input("Enter Bond Rate : "))
    bond_date = input("Enter Maturity Date : ")
    
    My_Bond = Bond(Sym, Curr_Price, Quant, bond_rate, bond_date)
    print(My_Bond)
    print()
    Rate_income = My_Bond.Calculate_Rate()
    print(f'Rate Income : {Rate_income}')
    print()
    print(My_Bond)
    
    print("\n--- Creating Option ---")
    strike = float(input("Enter Strike Price: "))
    exp_date = input("Enter Expiration Date: ")
    opt_type = input("Enter Option Type (Call/Put): ")
    
    My_Option = Option(Sym, Curr_Price, Quant, strike, exp_date, opt_type)
    print(My_Option)
    print()
    if My_Option.is_in_the_money():
        print("Good news! The option is currently profitable.")
    else:
        print("Note: The option is currently not profitable.")
    

if __name__ =="__main__":
    main()
    
    
    

