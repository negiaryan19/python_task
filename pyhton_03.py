stock_prices = {
    'APPL': 180,
    'TSLA': 250
}


portfolio = []

while True:
    stock_name = input("Enter stock name (or press Enter to stop): ").strip().upper()
    if stock_name == "":
        break
    if stock_name not in stock_prices:
        print("Sorry, that stock is not available. Try again.")
        continue
    quantity = input(f"Enter quantity for {stock_name}: ")
    try:
        quantity = int(quantity)
        if quantity <= 0:
            print("Quantity must be more than 0. Try again.")
            continue
        price = stock_prices[stock_name]
        value = quantity * price
        portfolio.append((stock_name, quantity, price, value))
        print(f"Added {quantity} of {stock_name} for ${value}")
    except ValueError:
        print("Please enter a number for quantity. Try again.")


total_value = 0
if portfolio:
    print("\nYour Portfolio:")
    for stock_name, quantity, price, value in portfolio:
        print(f"{stock_name}: {quantity} shares at ${price} each = ${value}")
        total_value += value
    print(f"\nTotal Value: ${total_value}")
else:
    print("No stocks added.")


save = input("Save to file? (yes/no): ").strip().lower()
if save == "yes":
    filename = input("Enter filename: ").strip()
    with open(filename + ".txt", "w") as file:
        file.write("Stock Portfolio\n")
        for stock_name, quantity, price, value in portfolio:
            file.write(f"{stock_name}: {quantity} @ ${price} = ${value}\n")
        file.write(f"Total: ${total_value}\n")
    print("Saved to " + filename + ".txt")
else:
    print("Not saved.")