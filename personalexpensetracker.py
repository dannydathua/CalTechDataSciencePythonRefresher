from datetime import datetime
import csv
expenses = []
budget = 0

def add_expense():
  try:
    ## validate date
    ## validate category
    ## validate amount
    ## validate description
    date = input("Enter + the date (YYYY-MM-DD): ")
    datetime.strptime(date, "%Y-%m-%d")
    amount = float(input("Enter the expense amount: "))
    category = input("Enter category (e.g., Food, Travel, Entertainment): ").strip()
    description = input("Enter the expense description: ")
    expenses.append({
      "date": date,
      "amount": amount,
      "category": category,
      "description": description
    })
    print("Expense added successfully!")
  except ValueError:
    print("Invalid expense input. Please reenter.")

def view_expenses():
  if expenses is None:
    print("No expense.")
  else:
    print("\nExpense History:")
    print("\nYour Expenses:")
  print(f"{'Date':<15}{'Category':<15}{'Amount':<10}{'Description'}")
  print("-" * 50)
  for expense in expenses:
      try:
          date = expense["date"]
          category = expense["category"]
          amount = expense["amount"]
          description = expense["description"]
          print(f"{date:<15}{category:<15}{amount:<10.2f}{description}")
      except KeyError as e:
          print(f"Incomplete entry found: {e}")



def set_budget():
  try:
    global budget
    budget = float(input("Enter your monthly budget: "))
    print("Budget set successfully!")
  except ValueError:
    print("Invalid budget input. Please reenter.")

def get_budget():
  print(f"Your Monthly budget is: {budget}")

def save_expenses():
  try:
    with open("expenses.csv", "w", newline='') as file:
      fieldnames = expenses[0].keys()
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(expenses)
      print(f"expenses.csv is written successfully!")
    with open('expenses.csv', 'r') as file:
      content = csv.reader(file)
      for r in content:
        print(r)
  except IOError:
    print("Error saving expenses.")


# Create another function that calculates the total expenses recorded so far
# o Compare the total with the user’s monthly budget
# o If the total expenses exceed the budget, display a warning (Example:
# You have exceeded your budget!)
# o If the expenses are within the budget, display the remaining balance
# (Example: You have 150 left for the month)
def track_budget():
  total_expenses = sum(expense["amount"] for expense in expenses)
  remaining_budget = budget - total_expenses
  if remaining_budget >0: 
    print(f"Remaining Budget: ${remaining_budget:.2f}")
  else:
    print(f"Warning: exceeded budget by: ${remaining_budget:.2f}")


def display_menu():
  while True:
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Set Budget")
    print("4. Track Budget")
    print("5. Save Expenses")
    print("6. Exit")
    try:
      choice = int(input("Enter your choice [1-6]: "))
      if choice == 1:
        add_expense()
      elif choice == 2:
        view_expenses()
      elif choice == 3:
        set_budget()
      elif choice == 4:
        track_budget()
      elif choice == 5:
        save_expenses()
      elif choice == 6:
        print("Exiting Personal Expense Tracker. Goodbye!")
        break
      else:
        print("Invalid input. Please choose again.")
    except ValueError:
      print("Invalid input. Please enter a number.")


display_menu()

