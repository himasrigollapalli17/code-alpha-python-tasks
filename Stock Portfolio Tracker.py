# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 200
}

total_investment = 0

# Number of stocks user wants to enter
n = int(input("Enter number of stocks: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # Check if stock exists
    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Investment for", stock_name, "=", investment)
    else:
        print("Stock not found!")

# Display total investment
print("\nTotal Investment Value =", total_investment)

# Save result into a text file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Result saved in portfolio.txt")