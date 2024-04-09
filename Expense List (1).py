

expense = input("Welcome to your Expense Tracker!\nHere you will be able to add your expenses with a description and amount. \nLet's start add your expense.\nSay 'yes'\n")

expenses = []

def add_expense():
    description = input("Enter expense description: ")
    category = input("Enter expense category: ")
    amount = None
    while amount is None:
            try:
                amount = float(input("Enter expense amount: "))
            except ValueError:
                print("Please enter a valid amount")
    expenses.append((category, description, amount))
    print("Expense added successfully!")
    while True:
        another_expense = input("Do you want to add another expense? (yes/no): ")
        if another_expense.lower() == "yes":
            add_expense()
            break
        elif another_expense.lower() == "no":
                display_expenses()
                print("What do you want to do?")
                print("1. Add an expense")
                print("2. Display expenses")
                print("3. Quit")
                choice = input("Enter the number of your choice: ")
                if choice.lower() == "1":
                    add_expense()
                    break
                elif choice.lower() == "2":
                    display_expenses()
                    break
                elif choice.lower() == "3":
                    print("Goodbye!")
                    break
                elif choice.lower()!= "yes":
                    print("You have entered an invalid input. Please enter 1, 2, or 3 to select an option.")
                    continue
                elif choice.lower() == "yes":
                    print("You have chosen to continue. Please select an option by entering 1, 2, or 3.")
        else:
            print("Please enter 'yes' or 'no'")

def display_expenses():
    with open("expenses.txt", "w") as f:
        for i, (category, description, amount) in enumerate(expenses, 1):
            f.write(f"{i}. {category} - {description}: ${amount}\n")
    with open("expenses.txt", "r") as f:
        print(f.read())

if expense.lower() == "yes":
    while True:
        print("What do you want to do?")
        print("1. Add an expense")
        print("2. Display expenses")
        print("3. Quit")
        choice = input("Enter the number of your choice: ")
        if choice.lower() == "1":
            add_expense()
            break
        elif choice.lower() == "2":
            display_expenses()
            break
        elif choice.lower() == "3":
            print("Goodbye!")
            break
        elif choice.lower()!= "yes":
            print("You have entered an invalid input. Please enter '1', '2', or '3' to select an option.")
            continue
        elif choice.lower() == "yes":
            print("You have chosen to continue. Please select an option by entering '1', '2', or '3'.")