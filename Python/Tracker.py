from expense import Expense
from Income import Income

def main():
    print(f"Running tracker!")
    #income = get_user_Income()
    #print(income)
    #Expense = get_user_Expense()
    #print(Expense)

    income_file_path = "income.csv"
    #save_user_Income(income,income_file_path)

    expense_file_path = "expense.csv"
    #save_user_Expense(Expense, expense_file_path)

    summerize_balance(income_file_path, expense_file_path)

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


#write the income to a file and expenser to the same file
def save_user_Income( income:Income, income_file_path):
    print(f"saving user income:{income} to {income_file_path}")
    with open(income_file_path , "a") as f:
       f.write(f" {income.source}, {income.type} , {income.amount}\n")
          

def save_user_Expense(expense:Expense, expense_file_path):
    print(f"saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path , "a" ) as f:
       f.write(f"{expense.name},{expense.category},{expense.type},{expense.amount}\n")

#read the file and summerize income expenses and show the avaialable balance
def summerize_balance(income_file_path , expense_file_path):
    

    print(f"summerize user income and expense")
    with open(income_file_path ,"r") as f:
       print("income")
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


    amount_by_type = {}
    for income in incomes:
       key = income.type
       if key in amount_by_type:
          amount_by_type[key] += income.amount
       else:
          amount_by_type[key] = income.amount
    print("\nincome by type ")
    for key , amount in  amount_by_type.items():
       print(f"{key}: Npr {amount:.2f}")
    

    with open(expense_file_path, "r") as f:
       print("expenses")
       expenses:list[Expense] = []
       lines = f.readlines()
       for line in lines:
        expense_name,expense_category,expense_type,expense_amount = line.strip().split(",")
        line_expense = Expense(name=expense_name,category=expense_category,type=expense_type,amount = float(expense_amount))
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

       total_in_category = sum([])


    amount_by_type = {}
    for expense in expenses:
       key = expense.type
       if key in amount_by_type:
          amount_by_type[key] += expense.amount
       else:
          amount_by_type[key] = expense.amount
    print("\nexpense by type ")
    for key , amount in  amount_by_type.items():
       print(f"{key}: Npr {amount:.2f}")



if __name__ == "__main__":
    main()
    