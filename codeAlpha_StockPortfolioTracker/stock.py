def stock_portfolio():

    print("==========================================")
    print("      📈 STOCK PORTFOLIO TRACKER")
    print("==========================================\n")
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "AMZN": 3300,
        "GOOGL": 2800,
        "MSFT": 320
    }

    print("Bot: Here are the available stock prices:\n")
    for stock, price in stock_prices.items():
        print(f"  • {stock}: ₹{price}")

    print("\nBot: Enter the stocks you purchased.")
    print("Type 'done' when you are finished.\n")

    portfolio = {}

    while True:
        symbol = input("Enter stock symbol: ").upper()

        if symbol == "DONE":
            break

        if symbol not in stock_prices:
            print("Bot: Invalid stock symbol. Try again.\n")
            continue

        qty = int(input(f"Enter quantity of {symbol}: "))

        portfolio[symbol] = portfolio.get(symbol, 0) + qty

        print(f"Bot: Added {qty} shares of {symbol}. (₹{qty * stock_prices[symbol]})\n")

    print("\n============ PORTFOLIO SUMMARY ============")

    total_value = 0
    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        value = price * qty
        total_value += value
        print(f"{symbol}: {qty} shares → ₹{value}")

    print("--------------------------------------------")
    print(f"Total Investment: ₹{total_value}")
    print("============================================\n")


    save = input("Do you want to save this report? (yes/no): ").lower()

    if save == "yes":
        with open("portfolio_report.txt", "w", encoding="utf-8") as file:
            file.write("STOCK PORTFOLIO REPORT\n\n")    
            for symbol, qty in portfolio.items():
                price = stock_prices[symbol]
                value = price * price
                value = qty * price
                file.write(f"{symbol}: {qty} shares → ₹{value}\n")

            file.write(f"\nTotal Investment: ₹{total_value}\n")

        print("Report saved to portfolio_report.txt")
    else:
        print("Report not saved.")

stock_portfolio()
