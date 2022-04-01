from asyncore import write
import mongobd as mdb
import printing as p
import validatation as v
import json

def record_sale():
    p.sale_print()
    # option = (validate_int(input("\nPlease select one option: ")))
    option = (v.validate_int(input("\nPlease select one option: ")))
    match option:
        case 0:
            return
        case 1:
            mdb.cash_sale()
            print("\nTransaction was recorded succesfully!")
        case 2:
            mdb.credit_sale()
        case _:
            print("\nInvalid input, you will go back to the main menu\n")

def record_purchase():
    p.purchase_print()
    option = (v.validate_int(input("\nPlease select one option: ")))
    match option:
        case 0:
            return
        case 1:
            mdb.cash_purchase()
            print("\nTransaction was recorded succesfully!")
        case 2:
            mdb.credit_purchase()
            print("\nTransaction was recorded succesfully!")
        case _:
            print("\nInvalid input, you will go back to the main menu\n")

def record_owners():
    p.owners_print()
    option = (v.validate_int(input("\nPlease select one option: ")))
    match option:
        case 0:
            return
        case 1:
            mdb.owner_deposit()
            print("\nTransaction was recorded succesfully!")
        case 2:
            mdb.owner_withdrawal()
            print("\nTransaction was recorded succesfully!")
        case _:
            print("\nInvalid input, you will go back to the main menu\n")

def record_deferrrals():
    p.deferrals_print()
    option = (v.validate_int(input("\nPlease select one option: ")))
    match option:
        case 0:
            return
        case 1:
            mdb.receivables()
            print("\nTransaction was recorded succesfully!")
        case 2:
            mdb.payables()
            print("\nTransaction was recorded succesfully!")
        case _:
            print("\nInvalid input, you will go back to the main menu\n")

def show_reports():
    p.reports_print()
    option = (v.validate_int(input("Please select one option: ")))
    match option:
        case 0:
            return
        case 1:
            mdb.view_ledger()  
        case 2:
            
        case 3:
            # TODO: mongodb->debit acc receivables and cogs, credit inventory, and revenue
            print("\nTransaction was recorded succesfully!")
        case _:
            print("\nInvalid input, you will go back to the main menu\n")

def record_customer_changes():
    p.customer_print()
    option = (v.validate_int(input("Please select one option: ")))
    match option:
        case 0:
            return
        case 1:
            mdb.upsert_cust()
            print("\nCustomer added/updated succesfully! \n")
        case 2:
            mdb.view_cust()
            return False
        case 3:
            mdb.delete_cust()
            print("\nCustomer deleted succesfully! \n")
        case _:
            print("\nInvalid input, you will go back to the main menu\n")
        
    return True

def load_data():
    file_name = input("\nPlease provide Data to load: Customers or Inv_Shirts ")
    if file_name in ['Customers', 'Inv_Shirts']:
        file_path = f'data/{file_name}.json'    
        with open(file_path, 'r') as file:
            file_data = json.load(file)
        
        mdb.load_data_to_db(file_name, file_data)
        print("\nData lodaded succesfullly! \n")
    else:
        print("\nInvalid file name, going back to main menu... ")
