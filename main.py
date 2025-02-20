import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"]
    DATE_FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        cls.initialize_csv()
        new_entry = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description,
        }

        with open(cls.CSV_FILE, "a", newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        
        print("Entry added successfully.")

    @classmethod
    def add_input_entry(cls):
        date = get_date("Enter the date of transaction in 'DD-MM-YYYY' format or press Enter for today's date: ", True)
        amount = get_amount()
        category = get_category()
        description = get_description()

        cls.add_entry(date, amount, category, description)

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)

        df["Date"] = pd.to_datetime(df["Date"], format=cls.DATE_FORMAT)
        start_date = datetime.strptime(start_date, cls.DATE_FORMAT)
        end_date = datetime.strptime(end_date, cls.DATE_FORMAT)
        filtered_df = df[ (df["Date"] >= start_date) & (df["Date"] <= end_date) ]
        if filtered_df.empty:
            print("No transactions found withing the specified date range.")
        else:
            print(f"Transactions from {start_date.strftime(cls.DATE_FORMAT)} to {end_date.strftime(cls.DATE_FORMAT)} are listed below.")
            print(filtered_df.to_string(index=False, 
                                        formatters={"Date": lambda x: x.strftime(cls.DATE_FORMAT)}))

            total_income = filtered_df[ (filtered_df["Category"] == "Income") ]["Amount"].sum()
            total_expense = filtered_df[ (filtered_df["Category"] == "Expense") ]["Amount"].sum()
            print("\nSummary of the transactions:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: {(total_income - total_expense):.2f}")
        
        return filtered_df
        
    @classmethod
    def plot_transactions(cls, df):
        df.set_index("Date", inplace=True)

        income_df = (
            df[ (df["Category"] == "Income") ]
            .resample("D")
            .sum()
            .reindex(df.index, fill_value=0)
        )
        expense_df = (
            df[ (df["Category"] == "Expense") ]
            .resample("D")
            .sum()
            .reindex(df.index, fill_value=0)
        )

        plt.figure(figsize=(10, 5))
        plt.plot(income_df.index, income_df["Amount"], label="Income", color="g")
        plt.plot(expense_df.index, expense_df["Amount"], label="Expense", color="r")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.title("Income and Expenses over time")
        plt.legend()
        plt.show()


def main():
    while True:
        print("\n1. Add a new transaction.")
        print("2. View transactions and summary within a date range.")
        print("3. Exit.")

        choice = input("Enter choice: ")
        if choice == "1":
            CSV.add_input_entry()
        elif choice == "2":
            start_date = get_date("Enter the start date in 'DD-MM-YYYY' format: ")
            end_date = get_date("Enter the end date in 'DD-MM-YYYY' format: ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n): ").lower() == "y":
                CSV.plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()