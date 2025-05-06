# DATA 200 – Lab 2: Stock Analyzer

This project is a console-based stock analysis tool for managing stock data, importing/exporting daily records, retrieving data from the web, and visualizing trends using charts.

## Included Files

- `stock_console.py` – Main program file for interacting with the stock analyzer via console.
- `stocks.py` – Shortcut script to launch the stock console.
- `stock_class.py` – Contains Stock and DailyData class definitions.
- `stock_data.py` – Handles stock-related data operations and validation.
- `utilities.py` – Includes functions for clearing the screen and displaying charts.
- `chromedriver` – Required for web data scraping using Selenium.
- `generate_csv.ipynb` – Jupyter notebook that generates `aapl_data.csv` using Yahoo Finance.
- `aapl_data.csv` – Sample file to test CSV import functionality.
- `stock_data.pkl` – Binary data file used internally by `generate_csv.ipynb`.

## How to Run the Project

1. Place all the files in the same directory.

2. Open a terminal and navigate to that folder.

3. Run the program using either command:
   ```bash
   python3 stock_console.py
   # or
   python3 stocks.py
   ```

4. Use the menu to:
   - Add, update, or delete stock entries
   - Input daily stock data (price/volume)
   - View reports and charts
   - Save/load the database
   - Import from CSV
   - Retrieve data from the web using Selenium

5. If `aapl_data.csv` is missing, open `generate_csv.ipynb` in Jupyter Notebook and run all cells. This uses Yahoo Finance to create the CSV using `stock_data.pkl`.

## Dependencies

Install required packages with:

```bash
pip install yfinance matplotlib selenium beautifulsoup4 pandas
```

Make sure `chromedriver` is in the same directory and compatible with your version of Google Chrome.

---

**Author:** Keon Sadeghi 
**Course:** DATA 200 – San José State University
