# monthly_report.py

def calculate_summary(income, expenses):
    total_income = sum(income)
    total_expenses = sum(expenses)
    balance = total_income - total_expenses

    print("=== Monthly Summary ===")
    print(f"Total Income: ₹{total_income}")
    print(f"Total Expenses: ₹{total_expenses}")
    print(f"Balance: ₹{balance}")

# Example usage
calculate_summary([5000, 3000, 2000], [2500, 1500, 1000])
