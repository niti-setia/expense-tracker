import os
import datetime

def initialize_file():
    if not os.path.exists('expenses.txt'):
        with open('expenses.txt', 'w') as file:
            file.write('Date,Amount,Category,Description\n')

def add_expense(date, amount, category, description):
    with open('expenses.txt', 'a') as file:
        file.write(f'{date},{amount},{category},{description}\n')
    print("✅ Expense added")

def view_expenses():
    with open('expenses.txt', 'r') as file:
        lines = file.readlines()
        print("\n📋 All Expenses:")
        print(lines[0].strip())
        for line in lines[1:]:
            print(line.strip())

def filter_expenses(filter_by, filter_value):
    with open('expenses.txt', 'r') as file:
        lines = file.readlines()
        print(f"\n🔎 Filtered by {filter_by}: {filter_value}")
        print(lines[0].strip())
        for line in lines[1:]:
            data = line.strip().split(',')
            if filter_by == 'date' and filter_value == data[0]:
                print(line.strip())
            elif filter_by == 'category' and filter_value == data[2]:
                print(line.strip())

def delete_expenses(date, amount, category, description):
    with open('expenses.txt', 'r') as file:
        lines = file.readlines()
    with open('expenses.txt', 'w') as file:
        for line in lines:
            if line.strip() != f'{date},{amount},{category},{description}':
                file.write(line)
    print("🗑️ Expense deleted")

def monthly_summary():
    current_month = datetime.datetime.now().strftime('%Y-%m')
    total_expense = 0.0
    category_expense = {}

    with open('expenses.txt', 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:
        data = line.strip().split(',')
        if data[0].startswith(current_month):
            amount = float(data[1])
            category = data[2]
            total_expense += amount
            category_expense[category] = category_expense.get(category, 0.0) + amount

    print(f'\n📅 Total expense for {current_month}: ₹{total_expense:.2f}')
    for category, amount in category_expense.items():
        print(f'   {category}: ₹{amount:.2f}')
