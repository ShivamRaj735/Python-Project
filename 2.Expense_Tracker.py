import matplotlib.pyplot as plt

expenses = []

budgets = {
    "Food": 500,
    "Transport": 300,
    "Entertainment": 200,
    "Other": 400
}

def add_expense():
    category = input("Enter category (Food, Transport, Entertainment, Other): ")
    amount = float(input("Enter amount: "))
    expenses.append({"category": category, "amount": amount})
    print("Expense added!\n")

def show_summary():
    print("\n=== Expense Summary ===")
    totals = {}
    for expense in expenses:
        cat = expense["category"]
        amt = expense["amount"]
        totals[cat] = totals.get(cat, 0) + amt

    for cat, total in totals.items():
        print(f"{cat}: ₹{total}")
        if cat in budgets and total > budgets[cat]:
            print(f"Overspent in {cat}! Budget: ₹{budgets[cat]}")

def show_chart():
    totals = {}
    for expense in expenses:
        cat = expense["category"]
        amt = expense["amount"]
        totals[cat] = totals.get(cat, 0) + amt

    if not totals:
        print("No data to show.")
        return

    
    categories = list(totals.keys())
    amounts = list(totals.values())
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Spending Chart")
    plt.show()


def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show Summary")
        print("3. Show Chart")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_chart()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

menu()
