stocks = {
    "A": 3500,
    "B": 1600,
    "C": 2900,
    "D": 1700,
    "E": 450
}

stock_name = input("Enter stock name: ").upper()

if stock_name in stocks:
    quantity = int(input("Enter quantity: "))

    total = stocks[stock_name] * quantity

    print("\n----- Stock Details -----")
    print("Stock Name :", stock_name)
    print("Price      :", stocks[stock_name])
    print("Quantity   :", quantity)
    print("Total Cost :", total)

    choice = input("\nDo you want to save the details? (yes/no): ").lower()

    if choice == "yes":
        file = open("stock_details.txt", "w")
        file.write("Stock Name: " + stock_name + "\n")
        file.write("Price: " + str(stocks[stock_name]) + "\n")
        file.write("Quantity: " + str(quantity) + "\n")
        file.write("Total Cost: " + str(total))
        file.close()
        print("Details saved successfully!")
else:
    print("Stock not available.")