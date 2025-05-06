# Helper Functions

import matplotlib.pyplot as plt
from os import system, name

# Function to Clear the Screen
def clear_screen():
    if name == "nt":  # User is running Windows
        _ = system('cls')
    else:  # User is running Linux or Mac
        _ = system('clear')

# Function to sort the stock list (alphabetical)
def sortStocks(stock_list):
    stock_list.sort(key=lambda stock: stock.symbol)

# Function to sort the daily stock data (oldest to newest) for all stocks
def sortDailyData(stock_list):
    for stock in stock_list:
        stock.DataList.sort(key=lambda day: day.date)

# Function to create stock chart
def display_stock_chart(stock):
    if len(stock.DataList) == 0:
        print("No historical data to display.")
        input("Press Enter to return to menu.")
        return

    # Sort data by date
    stock.DataList.sort(key=lambda x: x.date)

    dates = [day.date for day in stock.DataList]
    prices = [day.close for day in stock.DataList]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o')
    plt.title(f"{stock.name} ({stock.symbol}) - Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()