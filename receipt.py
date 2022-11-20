import csv
def main():
    try:
        file_num = 0
        product_dict = read_dictionary("products.csv", file_num)
        print("All Products")
        print(product_dict)

        request_list = []
        with open ("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            for reqs in reader:
                request_list.append(reqs)
        
        amount_list = []
        price_list = []
        print("Inkom Emporium")
        print()
        for sum in request_list:
            list_reqs = sum[0]
            list_of_amount = int(sum[1])
            reqs_list = product_dict[list_reqs]
            item = reqs_list[1]
            price = float(reqs_list[2])
            amount_list.append(list_of_amount)
            price_list.append(price)
            print(f"{item}: {list_of_amount} @ {price}")

        for prices in range(len(price_list)):
            price_amount = amount_list[prices]*price_list[prices] + amount_list[prices - 1]*price_list[prices - 1] + amount_list[prices - 2]*price_list[prices - 2] + amount_list[prices - 3]*price_list[prices - 3] + amount_list[prices - 4]*price_list[prices - 4]
            amount_of_items = amount_list[prices] + amount_list[prices - 1] + amount_list[prices - 2] + amount_list[prices - 3] + amount_list[prices - 4]

        

            
        print()
        tax = round(price_amount * 0.06, 2)
        total = round(price_amount + tax, 2)
        print(f"Number of Items: {amount_of_items}")
        print(f"Subtotal: {price_amount}")
        print(f"Sales Tax: {tax}")
        print(f"Total: {total}")
        print()
        print("Thank you for shoppibng at the Inkom Emporium.")

        
        # Import the datetime class from the datetime
        # module so that it can be used in this program.
        from datetime import datetime

        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()

        # Use an f-string to print the current
        # day of the week and the current time.
        print(f"{current_date_and_time:%A %I:%M %p}")

    except KeyError as key:
        print()
        print("Error: unknown product ID in the request.csv file")
        print(key, sep=": ")

    except FileNotFoundError as no_file:
        print()
        print("Error: missing file")
        print(no_file, sep=": ")
        
    

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
    product_dictionaries = {}
    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        for row_list in reader:
            key = row_list[key_column_index]
            product_dictionaries[key] = row_list
    return product_dictionaries


main()