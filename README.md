# Your-Personal-Finance-Tracker
The Personal Finance Tracker project is designed to help individuals effectively manage and monitor their finances. This program enables users to log all transactions, capturing essential details such as the transaction date, type (income or expense), and an optional short description. The tracker also provides a summary of transactions within a specified date range, offering users a comprehensive view of their financial activity. Additionally, the program includes the option to generate a simple plot, helping users visualize their financial trends and make more informed decisions about budgeting and saving.

The `main.py` file serves as the entry point for the program. Upon logging the first transaction, it automatically creates a `finance_data.csv` file, storing the transaction details in CSV format if the file doesn't already exist. For subsequent transactions, the program appends the new details to the end of the existing `finance_data.csv` file. If the file is created manually, it must be placed in the same folder as the `main.py` or `data_entry.py` files for proper functionality. The project includes a dummy `finance_data.csv` file for initial use, but users can easily remove it and create their own file with a similar structure to suit their needs.

To run the program, the user must have the `pandas` module installed for proper file handling and the `matplotlib` module for generating plots. Once these dependencies are installed, the rest of the program's functionality is straightforward and can be easily understood as the user interacts with it.

This project enhanced my Python coding skills while providing a basic understanding of the `pandas` and `matplotlib` libraries, both of which are widely used in data engineering for data manipulation and visualization. It gave me practical experience with these tools, preparing me for more advanced data engineering tasks.




