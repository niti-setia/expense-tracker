from exp_trac_fun import *

print('📊 Personal Expense Tracker 📊'.center(50, '-'))

def main():
    initialize_file()
    while True:
        print('\nMain Menu:')
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Filter Expenses')
        print('4. Delete Expense')
        print('5. Monthly Summary')
        print('6. Exit')

        choice = input('\nSelect an option (1-6): ')

        if choice == '1':
            date = input("Enter date (yyyy-mm-dd): ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(date, amount, category, description)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            filter_by = input("Filter by (date/category): ").strip().lower()
            filter_value = input(f"Enter {filter_by}: ")
            filter_expenses(filter_by, filter_value)

        elif choice == '4':
            date = input("Enter date (yyyy-mm-dd): ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            delete_expenses(date, amount, category, description)

        elif choice == '5':
            monthly_summary()

        elif choice == '6':
            print("👋 Exiting the program. Bye!")
            break

        else:
            print("❌ Invalid option. Please select from 1–6.")

if __name__ == '__main__':
    main()
