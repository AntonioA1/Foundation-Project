from printing import menu, welcome_msg
import recording as r 
import time         
import os

def main():
    welcome_msg()
    while(True):
        clear_screen = True
        optionSelected = menu() # int(menu)
        match optionSelected:
            case 0:
                return
            case 1:
                r.record_sale()
            case 2:
                r.record_purchase()
            case 3:
                r.record_owners()
            case 4:
                r.record_deferrrals()
            case 5:
                r.show_reports()
                clear_screen = False
            case 6:
                clear_screen = r.record_customer_changes()
            case 7:
                r.load_data()
            case _:
                print("\nInvalid input, please try again.\n")
        if clear_screen:
            time.sleep(2)
            os.system('cmd /c "cls"')
        else:
            input("\nEnter any character to go back to main menu")

if __name__ == "__main__":
    main()