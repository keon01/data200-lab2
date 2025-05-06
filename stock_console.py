# Summary: This module contains the user interface and logic for a console-based version of the stock manager program.

from datetime import datetime
from stock_class import Stock, DailyData
from utilities import clear_screen, display_stock_chart
from os import path
import stock_data
import pickle
from stock_data import is_valid_ticker

# Main Menu
def main_menu(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Stock Analyzer ---")
        print("1 - Manage Stocks (Add, Update, Delete, List)")
        print("2 - Add Daily Stock Data (Date, Price, Volume)")
        print("3 - Show Report")
        print("4 - Show Chart")
        print("5 - Manage Data (Save, Load, Retrieve)")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","5","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("Stock Analyzer ---")
            print("1 - Manage Stocks (Add, Update, Delete, List)")
            print("2 - Add Daily Stock Data (Date, Price, Volume)")
            print("3 - Show Report")
            print("4 - Show Chart")
            print("5 - Manage Data (Save, Load, Retrieve)")
            print("0 - Exit Program")
            option = input("Enter Menu Option: ")
        if option == "1":
            manage_stocks(stock_list)
        elif option == "2":
            add_stock_data(stock_list)
        elif option == "3":
            display_report(stock_list)
        elif option == "4":
            display_chart(stock_list)
        elif option == "5":
            manage_data(stock_list)
        else:
            clear_screen()
            print("Goodbye")

# Manage Stocks
def manage_stocks(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Stocks ---")
        print("1 - Add Stock")
        print("2 - Update Shares")
        print("3 - Delete Stock")
        print("4 - List Stocks")
        print("0 - Exit Manage Stocks")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("1 - Add Stock")
            print("2 - Update Shares")
            print("3 - Delete Stock")
            print("4 - List Stocks")
            print("0 - Exit Manage Stocks")
            option = input("Enter Menu Option: ")
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            update_shares(stock_list)
        elif option == "3":
            delete_stock(stock_list)
        elif option == "4":
            list_stocks(stock_list)
        else:
            print("Returning to Main Menu")

# Add new stock to track
def add_stock(stock_list):
    while True:
        clear_screen()
        print("Add New Stock ---")
        symbol = input("Enter stock symbol (or 0 to cancel): ").upper()
        if symbol == "0":
            break
            
        official_name = is_valid_ticker(symbol)
        if not official_name:
            print(f"{symbol} is not a valid ticker symbol. Press Enter to try again.")
            input()
            continue

        entered_name = input("Enter company name: ").strip()
        if entered_name.lower() != official_name.lower():
            print(f"That doesn’t match the official name for {symbol.upper()}, which is:\n-> {official_name}")
            confirm = input("Use the correct name instead? (Y/N): ").strip().lower()
            if confirm == "y":
                name = official_name
            else:
                print("Stock not added. Press Enter to try again.")
                input()
                continue  # restart loop
        else:
            name = entered_name

        try:
            shares = float(input("Enter number of shares: "))
        except:
            print("Invalid number of shares. Press Enter to try again.")
            input()
            continue

        exists = False
        for stock in stock_list:
            if stock.symbol == symbol:
                exists = True
                break
        if exists:
            print("Stock already exists. Press Enter to try again.")
            input()
            continue

        new_stock = Stock(symbol, name, shares)
        stock_list.append(new_stock)
        print(f"Stock {symbol} added. Press Enter to continue.")
        input()
        break

# Buy or Sell Shares Menu
def update_shares(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Update Shares ---")
        print("1 - Buy Shares")
        print("2 - Sell Shares")
        print("0 - Return to Manage Stocks Menu")
        option = input("Enter Menu Option: ")

        while option not in ["1", "2", "0"]:
            print("*** Invalid Option - Try again ***")
            option = input("Enter Menu Option: ")

        if option == "1":
            buy_stock(stock_list)
        elif option == "2":
            sell_stock(stock_list)

# Buy Stocks (add to shares)
def buy_stock(stock_list):
    clear_screen()
    print("Buy Shares ---")
    if len(stock_list) == 0:
        print("No stocks available.")
        input("Press Enter to return to menu.")
        return

    for idx, stock in enumerate(stock_list):
        print(f"{idx+1} - {stock.symbol} ({stock.name})")

    try:
        selection = int(input("Enter stock number: "))
        if 1 <= selection <= len(stock_list):
            amount = float(input("Enter number of shares to buy: "))
            stock_list[selection - 1].buy(amount)
            print("Shares added.")
        else:
            print("Invalid stock selection.")
    except:
        print("Invalid input.")
    input("Press Enter to return to menu.")

# Sell Stocks (subtract from shares)
def sell_stock(stock_list):
    clear_screen()
    print("Sell Shares ---")
    if len(stock_list) == 0:
        print("No stocks available.")
        input("Press Enter to return to menu.")
        return

    for idx, stock in enumerate(stock_list):
        print(f"{idx+1} - {stock.symbol} ({stock.name})")

    try:
        selection = int(input("Enter stock number: "))
        if 1 <= selection <= len(stock_list):
            amount = float(input("Enter number of shares to sell: "))
            if amount > stock_list[selection - 1].shares:
                print("You don't have that many shares.")
            else:
                stock_list[selection - 1].sell(amount)
                print("Shares subtracted.")
        else:
            print("Invalid stock selection.")
    except:
        print("Invalid input.")
    input("Press Enter to return to menu.")

# Remove stock and all daily data
def delete_stock(stock_list):
    clear_screen()
    print("Delete Stock ---")
    if len(stock_list) == 0:
        print("No stocks available to delete.")
        input("Press Enter to return to menu.")
        return

    for idx, stock in enumerate(stock_list):
        print(f"{idx+1} - {stock.symbol} ({stock.name})")

    try:
        selection = int(input("Enter stock number to delete: "))
        if 1 <= selection <= len(stock_list):
            deleted_stock = stock_list.pop(selection - 1)
            print(f"Deleted {deleted_stock.symbol} - {deleted_stock.name}")
        else:
            print("Invalid stock number.")
    except:
        print("Invalid input.")
    input("Press Enter to return to menu.")


# List stocks being tracked
def list_stocks(stock_list):
    clear_screen()
    print("Tracked Stocks ---")
    if len(stock_list) == 0:
        print("No stocks added.")
    else:
        for stock in stock_list:
            print(f"{stock.symbol} - {stock.name} | Shares: {stock.shares}")
    input("\nPress Enter to return to menu.")

# Add Daily Stock Data
def add_stock_data(stock_list):
    clear_screen()
    print("Add Daily Stock Data ---")
    if len(stock_list) == 0:
        print("No stocks available.")
        input("Press Enter to return to menu.")
        return

    for idx, stock in enumerate(stock_list):
        print(f"{idx+1} - {stock.symbol} ({stock.name})")

    try:
        selection = int(input("Enter stock number: "))
        if 1 <= selection <= len(stock_list):
            selected_stock = stock_list[selection - 1]
        else:
            print("Invalid selection.")
            input("Press Enter to return to menu.")
            return
    except:
        print("Invalid input.")
        input("Press Enter to return to menu.")
        return

    try:
        date_str = input("Enter date (MM/DD/YY): ")
        date = datetime.strptime(date_str, "%m/%d/%y")
        price = float(input("Enter closing price: "))
        volume = int(input("Enter volume: "))
        daily_data = DailyData(date, price, volume)
        selected_stock.add_data(daily_data)
        print("Data added successfully.")
    except:
        print("Invalid input. Failed to add data.")
    input("Press Enter to return to menu.")



# Display Report for All Stocks
def display_report(stock_data):
    clear_screen()
    print("Stock Report ---")
    for stock in stock_data:
        print(f"\n{stock.symbol} - {stock.name} | Shares: {stock.shares}")
        if len(stock.DataList) == 0:
            print("  No historical data.")
        else:
            print("  Date       | Price    | Volume")
            print("  -------------------------------")
            for day in stock.DataList:
                print(f"  {day.date.strftime('%m/%d/%y')} | ${day.close:8.2f} | {int(day.volume)}")
    input("\nPress Enter to return to menu.")

def display_chart(stock_list):
    clear_screen()
    print("Show Chart ---")
    if len(stock_list) == 0:
        print("No stocks available.")
        input("Press Enter to return to menu.")
        return
    for idx, stock in enumerate(stock_list):
        print(f"{idx+1} - {stock.symbol} ({stock.name})")
    selection = input("Enter stock number to view chart: ")
    if selection.isdigit():
        selection = int(selection)
        if 1 <= selection <= len(stock_list):
            display_stock_chart(stock_list[selection - 1])
        else:
            print("Invalid selection.")
    else:
        print("Invalid input.")
    input("Press Enter to return to menu.")

def manage_data(stock_list):
    while True:
        print("Manage Data ---")
        print("1 – Save Data to Database")
        print("2 – Load Data from Database")
        print("3 – Retrieve Data from Web")
        print("4 – Import from CSV File")
        print("0 – Exit Manage Data")
        option = input("Enter Menu Option: ")

        if option == "1":
            save_data(stock_list)
        elif option == "2":
            stock_list[:] = load_data()
        elif option == "3":
            retrieve_from_web(stock_list)
        elif option == "4":
            import_csv(stock_list)
        elif option == "0":
            break
        else:
            print("Invalid input. Try again.")

# Get stock price and volume history from Yahoo! Finance using Web Scraping
def retrieve_from_web(stock_list):
    clear_screen()
    print("Retrieve Data from Web ---")
    
    if len(stock_list) == 0:
        print("No stocks to update.")
        input("Press Enter to return to menu.")
        return

    print("Tracked Stocks:")
    for stock in stock_list:
        print(f"- {stock.symbol} ({stock.name})")
    
    date_start = input("Enter start date (MM/DD/YY): ")
    date_end = input("Enter end date (MM/DD/YY): ")

    try:
        record_count = stock_data.retrieve_stock_web(date_start, date_end, stock_list)
        print(f"\n{record_count} records retrieved and added successfully.")
    except RuntimeWarning as e:
        print(f"{e}")
    except Exception as e:
        print("Error retrieving data:", e)

    input("\nPress Enter to return to menu.")


# Import stock price and volume history from Yahoo! Finance using CSV Import
def import_csv(stock_list):
    clear_screen()
    print("Import from CSV ---")

    if len(stock_list) == 0:
        print("No stocks available.")
        input("Press Enter to return to menu.")
        return

    print("Tracked Stocks:")
    for stock in stock_list:
        print(f"- {stock.symbol} ({stock.name})")

    symbol = input("Enter stock symbol to import data into: ").upper()
    filename = input("Enter CSV filename (e.g. aapl_data.csv): ")

    # Check if symbol exists in the tracked list
    if not any(stock.symbol.lower() == symbol.lower() for stock in stock_list):
        print("Symbol not found in tracked stocks.")
        input("Press Enter to return to menu.")
        return  # Prevents it from continuing

    try:
        stock_data.import_stock_web_csv(stock_list, symbol, filename)
        print("CSV data imported successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error importing CSV: {e}")

    input("Press Enter to return to menu.")


# Function to save the stock list using pickle for persistent storage
def save_data(stock_list):
    try:
        with open("stock_data.pkl", "wb") as file:
            pickle.dump(stock_list, file)
        print("--- Data Saved to Database ---")
    except Exception as e:
        print("Error saving data:", e)
    input("Press Enter to Continue")

# Function to load the stock list using pickle for persistent storage
def load_data():
    try:
        with open("stock_data.pkl", "rb") as file:
            stock_list = pickle.load(file)
        print("--- Data Loaded from Database ---")
        input("Press Enter to Continue")
        return stock_list
    except FileNotFoundError:
        print("No saved data found.")
        input("Press Enter to Continue")
        return []
    except Exception as e:
        print("Error loading data:", e)
        input("Press Enter to Continue")
        return []


# Begin program
def main():
    #check for database, create if not exists
    if path.exists("stocks.db") == False:
        stock_data.create_database()
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()