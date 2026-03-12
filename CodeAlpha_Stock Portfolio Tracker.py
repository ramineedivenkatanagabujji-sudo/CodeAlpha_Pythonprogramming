
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

portfolio = {}
total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in prices:
        portfolio[stock] = quantity
    else:
        print("Stock not available")

for stock in portfolio:
    value = prices[stock] * portfolio[stock]
    total += value

print("\nTotal Investment Value:", total)

file = open("investment.txt", "w")
file.write("Total Investment Value: " + str(total))
file.close()

print("Result saved to investment.txt")