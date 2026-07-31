#!/usr/bin/env python
# coding: utf-8

# # Stock Portfolio Tracker
# Welcome to your Stock Portfolio Tracker. This notebook helps you calculate your total investment based on your stock quantities and predefined stock prices.
# 
# ### Features:
# 1. Predefined stock prices (Dictionary)
# 2. User input for stock names and quantities
# 3. Total investment calculation
# 4. Auto-save portfolio to a CSV file

# ### Step 1: Define Stock Prices
# We use a Python dictionary to store the current market prices of available stocks.

# In[1]:


# Predefined stock price database
STOCK_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 150.0,
    "MSFT": 400.0,
    "AMZN": 175.0
}

print("Available Stocks and Prices:")
for stock, price in STOCK_PRICES.items():
    print(f"- {stock}: ${price}")


# ### Step 2: Build the Portfolio Tracker
# Run this cell to input your stocks, calculate total values, and save your portfolio to a CSV file.

# In[ ]:


import csv

def run_portfolio_tracker():
    portfolio = {}
    total_investment = 0.0

    print("--- Enter Your Portfolio Details ---")
    print("(Type 'done' when you are finished adding stocks)\n")

    while True:
        stock_name = input("Enter stock name (e.g., AAPL): ").strip().upper()

        if stock_name == 'DONE':
            break

        if stock_name not in STOCK_PRICES:
            print(f"❌ {stock_name} is not in our database. Please try another stock.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("❌ Quantity must be greater than 0.\n")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a whole number for quantity.\n")
            continue

        # Add or update portfolio
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"✅ Added {quantity} shares of {stock_name}.\n")

    if not portfolio:
        print("\nEmpty portfolio. No summary generated.")
        return

    # Display Summary Table
    print("\n===================================================")
    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Total Value':<15}")
    print("---------------------------------------------------")

    rows_to_save = []
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        stock_value = qty * price
        total_investment += stock_value

        print(f"{stock:<10}{qty:<12}${price:<11.2f}${stock_value:<14.2f}")
        rows_to_save.append([stock, qty, price, stock_value])

    print("---------------------------------------------------")
    print(f"{'TOTAL INVESTMENT:':<34}${total_investment:,.2f}")
    print("===================================================")

    # Step 3: Save to CSV File
    filename = "portfolio_summary.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Name", "Quantity", "Price Per Share", "Total Value"])
        writer.writerows(rows_to_save)
        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT", "", "", f"${total_investment:,.2f}"])

    print(f"\n💾 Portfolio successfully saved to '{filename}'!")

# Run the project
run_portfolio_tracker()


# In[ ]:




