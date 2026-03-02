# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()
    
    if stock_name == "DONE":
        break
    
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment
        
        print(f"{stock_name} Investment = {quantity} × {price} = {investment}")
    else:
        print("❌ Stock not found!")

print("\n💰 Total Investment Value =", total_investment)

# Optional: Save to file
save = input("Do you want to save result to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Total Investment Value: " + str(total_investment))
    print("✅ Data saved to portfolio.txt")

print("📌 Program Ended")