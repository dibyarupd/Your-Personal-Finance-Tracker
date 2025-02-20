from datetime import datetime

DATE_FORMAT = "%d-%m-%Y"
CATEGORIES = {
    "I": "Income",
    "E": "Expense",
}


# returns the date as a string object in the format s'DD-MM-YYYY'
def get_date(prompt, allow_default=False):
    date_str = input(prompt)

    if allow_default and not date_str:
        return datetime.today().strftime(DATE_FORMAT)
    
    try:
        valid_date = datetime.strptime(date_str, DATE_FORMAT)
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        print("Invalid date format. Kindly enter the date in the 'DD-MM-YYYY' format.")
        return get_date(prompt, allow_default)
    

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("The amount must be a non-negative, non-zero value. Please try again.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    

def get_category():
    category = input("Enter the category. 'I' for Income or 'E' for Expense: ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category entry. Please try again.")
    return get_category()


def get_description():
    return input("Enter some description (optional): ")
 


        