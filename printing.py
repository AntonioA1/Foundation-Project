import validatation as v

def welcome_msg():
    print("-------------------------\nWelcome to CL Accounting\n-------------------------\n")

def menu():
    print("-------------------------------------------------------\nMain Menu: Please select one of the options below: \n")
    print("1. Record Sale")
    print("2. Record Purchase")
    print("3. Record Owner's transaction")
    print("4. Record Receibables/Payables")
    print("5. View Reports")
    print("6. Manage Clients")
    print("7. Load Data")
    print("0. Exit")

    return (v.validate_int(input("\nPlease select one option: ")))
    
def sale_print():
    print("\nOk, Lets record a sale. Was this a cash sale?\n")
    print("1. Yes, cash was received at the moment of the sale.")
    print("2. No, the customer promised to pay later.")
    print("0. Go Back to main Menu")

def purchase_print():
    print("\nOk, Lets record a purchase. Did you pay cash?\n")
    print("1. Yes, I paid cash.")
    print("2. No, I promised to pay later.")
    print("0. Go Back to main Menu")

def owners_print():
    print("\nOk, Lets record an owner's transaction. is cash going in or out of the company?\n")
    print("1. In, Capital Investment.")
    print("2. Out, Capital Withdrawal.")
    print("0. Go Back to main Menu")

def deferrals_print():
    print("\nOk, Lets record a deffered cash transaction. is cash going in or out of the company?\n")
    print("1. In, Received payment from customer who bought on account")
    print("2. Out, Payment for Goods bought on account")
    print("0. Go Back to main Menu")

def reports_print():
    print("\nOk, Lets Take a look at the Reports. Which one would you like to take a look at?\n")
    print("1. Ledger")
    print("2. Income Statement")
    print("0. Go Back to main Menu")

def customer_print():
    print("Are you entering a new client or supplier?")
    print("1. Add/update customers")
    print("2. View current customers ")
    print("3. Delete customers ")
    print("0. Go Back to main Menu ")