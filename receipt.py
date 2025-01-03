import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime, timedelta
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
def main():
    # Index of the Product Number column
    # in the products.csv file.
    PRODUCT_NUMBER_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    PRODUCT_QUANTITY_INDEX = 1
    item_number = 0
    subtotal = 0
    # Read the contents of the products.csv into a
    # compound dictionary named products_dict. Use
    # the Product Numbers as the keys in the dictionary.
    products_dict = read_dictionary("products.csv", PRODUCT_NUMBER_INDEX)


    # Open a file named request.csv and store a reference
    # to the opened file in a variable named request_file.

    with open("request.csv", "rt") as request_file:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(request_file)
        # The first row of the CSV file contains column
        # headings and not data about a dental office,
        # so this statement skips the first row of the
        # CSV file.
        next(reader)
        print('Inkom Emporium')
        print('Requested Items:')
        # Read each row in the CSV file one at a time.
        # The reader object returns each row as a list.
        try:
            for row_list in reader:
                product_number = row_list[PRODUCT_NUMBER_INDEX]
                product_quantity = int(row_list[PRODUCT_QUANTITY_INDEX])
                # if product_number in products_dict:
                value = products_dict[product_number]
                name = value[PRODUCT_NAME_INDEX]
                price = float(value[PRODUCT_PRICE_INDEX])
                print(f'{name}: {product_quantity} @  {price}')
                item_number += product_quantity
                subtotal += price * product_quantity
                sales_tax = subtotal * .06
                total = subtotal + sales_tax
            print(f'Number of Items: {item_number}')
            print(f'Subtotal: {subtotal:.2f}')
            print(f'Sales Tax: {sales_tax:.2f}')
            print(f'Total: {total:.2f}')
            print('Thank you for shopping at the Inkom Emporium.')
        except KeyError as key_err:
            # print(type(key_err).__name__, key_err)
            print(f"Error: unknown product ID '{product_number}' in the request.csv file")
        
    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%c}")
   
    # print a reminder of how many days until the New Years Sale begins (Jan 
    # 1) at the bottom of the receipt.
    next_year = current_date_and_time.year + 1
    new_year_date = datetime(year=next_year, month=1, day=1)
    days_until_sale = (new_year_date - current_date_and_time).days
    print(f"\nReminder: Only {days_until_sale} days until our New Year's Sale on January 1!")

    # print a "return by" date that is 9:00 PM 30 days in the future at 
    # the bottom of the receipt.
    return_by_date = current_date_and_time + timedelta(days=30)
    return_by_date = return_by_date.replace(hour=21, minute=0, second=0, microsecond=0)
    print(f"Return By: {return_by_date.strftime('%Y-%m-%d %I:%M %p')}\n")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    try:
        with open(filename, "rt") as csv_file:
            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(csv_file)
            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(reader)
            # Read the rows in the CSV file one row at a time.
            # The reader object returns each row as a list.
            for row_list in reader:
                # If the current row is not blank, add the
                # data from the current to the dictionary.
                if len(row_list) != 0:
                    # From the current row, retrieve the data
                    # from the column that contains the key.
                    key = row_list[key_column_index]
                    # Store the data from the current
                    # row into the dictionary.
                    dictionary[key] = row_list
            # Return the dictionary.
        return dictionary
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)
# Call main to start this program.
if __name__ == "__main__":
    main()