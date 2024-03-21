from expense import Expense
from Income import Income
import calendar
import datetime

def main():
    while True:
        action = input("Enter 'income' to input income, 'expense' to input expense, 'summary' to summarize balance, or 'exit' to quit: ").lower()

        if action == 'income':
            income = get_user_Income()
            save_user_Income(income, "income.csv")
        elif action == 'expense':
            expense = get_user_Expense()
            save_user_Expense(expense, "expense.csv")
        elif action == 'summary':
            summerize_balance("income.csv", "expense.csv")
        elif action == 'exit':
            print("Exiting tracker.")
            break
        else:
            print("Invalid input. Please try again.")
money_type = ['Cash', 'Online Payment' , 'Bank' ]

#Get user input for income and expense
def get_user_Income():
    print(f"getting user income")
    income_source = str(input("enter income source "))
    income_amount = float(input("enter income amount "))

    while True:
     print("Select a type: ")
     for i, type_name in enumerate(money_type) :
       print(f" {i+1}.{type_name} ")
    
     value_range = f"[1 - {len(money_type)}]"

     selected_index = int(input(f"Enter a type {value_range}:"))-1

     if selected_index in range(len(money_type)):
      selected_incometype = money_type[selected_index]
      new_income = Income(source = income_source ,type = selected_incometype ,amount = income_amount  )
      return new_income
     else:
      print(f" Value is out of range")
     

def get_user_Expense():
    print(f"getting user expense")
    expense_name = input("enter expense name ")
    expense_category = [ 'Food & Drinks' , 'Rent', 'Bills' , 'Transport' , 'Shopping' , 'Miscellanous', 'Fun']
    expense_amount = float(input("enter expense amount "))
    
    while True:
        print("Select a category:")
        for i, category_name in enumerate(expense_category):
            print(f" {i + 1}. {category_name}")
        category_range = f"[1 - {len(expense_category)}]"
        expense_category_index = int(input(f"Enter a category {category_range}:")) - 1

        if expense_category_index in range(len(expense_category)):
            # Loop for selecting money type
            while True:
                print("Select a type: ")
                for i, type_name in enumerate(money_type):
                    print(f" {i + 1}. {type_name}")
                value_range = f"[1 - {len(money_type)}]"
                selected_index = int(input(f"Enter a type {value_range}:")) - 1
                
                if selected_index in range(len(money_type)):
                    selected_expensecat = expense_category[expense_category_index]
                    selected_expensetype = money_type[selected_index]
                    new_expense = Expense( name = expense_name ,category = selected_expensecat,  amount = expense_amount, type = selected_expensetype)
                    return new_expense
                else:
                    print("Value is out of range")
        else:
            print("Value is out of range")
            return


#write the income to a file and expenser to the files
def save_user_Income( income:Income, income_file_path):
    print(f"saving user income:{income} to {income_file_path}")
    with open(income_file_path , "a") as f:
       f.write(f" {income.source},{income.type},{income.amount}\n")
          

def save_user_Expense(expense:Expense, expense_file_path):
    print(f"saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path , "a" ) as f:
       f.write(f"{expense.name},{expense.category},{expense.type},{expense.amount}\n")

#read the file and summerize income expenses and show the avaialable balance
def summerize_balance(income_file_path , expense_file_path):
    
    print(f"summerize user income")
    with open(income_file_path ,"r") as f:
       incomes:list[Income]=[]
       lines = f.readlines()
       for line in lines:
        income_source, income_type , income_amount= line.strip().split(",")
        line_income = Income(source=income_source,type = income_type , amount = float(income_amount))
        incomes.append(line_income)

    amount_by_sources = {}
    for income in incomes:
        key = income.source
        if key in amount_by_sources:
           amount_by_sources[key] += income.amount
        else:
           amount_by_sources[key] = income.amount
    print("\nincome by Sources ")
    for key , amount in  amount_by_sources.items():
       print(f"{key}: Npr {amount:.2f}")


    income_by_type = {}
    for income in incomes:
       key = income.type
       if key in income_by_type:
          income_by_type[key] += income.amount
       else:
          income_by_type[key] = income.amount
    print("\nincome by type ")
    for key , amount in  income_by_type.items():
       print(f"{key}: Npr {amount:.2f}")
    
    total_income = sum([income.amount for income in incomes])
    print(f"\n Total Income: npr {total_income:.2f} ")
    
 
    print(f"\n summerize user expense")
    with open(expense_file_path, "r") as f:
       expenses:list[Expense] = []
       lines = f.readlines()
       for line in lines:
        expense_name , expense_category , expense_type , expense_amount= line.strip().split(",")
        line_expense = Expense( name=expense_name ,category = expense_category,type = expense_type,amount = float(expense_amount))
        expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
           amount_by_category[key] += expense.amount
        else:
           amount_by_category[key] = expense.amount
    print("\nexpense by Category ")
    for key , amount in  amount_by_category.items():
       print(f"{key}: Npr {amount:.2f}")
    

    expense_by_type = {}
    for expense in expenses:
       key = expense.type
       if key in expense_by_type:
          expense_by_type[key] += expense.amount
       else:
          expense_by_type[key] = expense.amount
    print("\nexpense by type ")
    for key , amount in  expense_by_type.items():
       print(f"{key}: Npr {amount:.2f}")

    total_expense = sum([expense.amount for expense in expenses])
    print(f"\n Total Expense: npr {total_expense:.2f} ")

    #remaining budget from both
    remaining_total_budget = total_income - total_expense
    print(f"remaining budget {remaining_total_budget}")

    #remaining budget based on type
    budget_by_type={}
    print("\n Money left in type=")
    for key in set(income_by_type.keys()) | set(expense_by_type.keys()):
       income_amount = income_by_type.get(key, 0)
       expense_amount = expense_by_type.get(key, 0)
       budget_by_type[key] = income_amount - expense_amount
    for key , amount in  budget_by_type.items():

       print(f"{key}: Npr {amount:.2f}")

#for date and time remaining
    now = datetime.datetime.now()

    days_left = calendar.monthrange(now.year, now.month)[1]

    remaining_day = days_left- now.day

    print("\n remaining days:" , remaining_day)
    
    day_budget = remaining_total_budget/remaining_day

    print(f"budget per day: Npr {day_budget:.2f}")


if __name__ == "__main__":
    main()
    