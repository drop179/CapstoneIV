from tabulate import tabulate  # import the tabulate module for pretty printing


# ========The beginning of the class==========


class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''

    def get_cost(self):
        return '${:.2f}'.format(self.cost)
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity

        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        return f"{self.country} {self.code} {self.product} ${self.cost:.2f} ({self.quantity} available)"
        '''
        Add a code to returns a string representation of a class.
        '''


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoes = []
# Open the file named "inventory.txt" and assign the file object to variable 'f'

# ==========Functions outside the class==============
with open('inventory.txt') as f:
    # Use the 'next' function to skip the header line
    # This assumes that the first line of the file is a header line that is not needed for creating Shoe objects
    try:
        next(f)  # Skip the header line
        # rest of the function code...
        for line in f:  # Loop through the remaining lines in the file
            # Split the line into a list of strings using comma as a separator
            data = line.strip().split(",")
            # Extract data from the list and assign to variables
            country = data[0]
            code = data[1]
            product = data[2]
            cost = float(data[3])
            quantity = int(data[4])
            # Create a new Shoe object with the extracted data
            shoe = Shoe(country, code, product, cost, quantity)
            # Append the new Shoe object to the list of shoes
            shoes.append(shoe)
    except StopIteration:  # Handle the case where the file is empty or has no data
        print("Error: File is empty or contains no data.")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def read_shoes_data():
        with open('inventory.txt') as f:
            try:
                next(f)  # Skip the header line
                for line in f:
                    fields = line.strip().split(',')
                    country = fields[0]
                    code = fields[1]
                    product = fields[2]
                    cost = float(fields[3])
                    quantity = int(fields[4])
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoes.append(shoe)
            except (FileNotFoundError, ValueError, IndexError) as e:
                print(f"Error reading shoes data: {e}")
        return shoes

        '''
        This function will open the file inventory.txt
        and read the data from this file, then create a shoes object with this data
        and append this object into the shoes list. One line in this file represents
        data to create one object of shoes. You must use the try-except in this function
        for error handling. Remember to skip the first line using your code.
        '''

    def capture_shoes():
        # call the function to add a shoe to the list
        country = input("Enter the country: ")
        code = input("Enter the code: ")
        product = input("Enter the product name: ")
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))
        shoe = Shoe(country, code, product, cost, quantity)
        shoes.append(shoe)

        # write the shoe to the inventory file
        with open("inventory.txt", "a") as file:
            file.write(f"{country},{code},{product},{cost},{quantity}\n")

        '''
        This function will allow a user to capture data
        about a shoe and use this data to create a shoe object
        and append this object inside the shoe list.
        '''

    # call the function to print all the shoes in the list
    def view_all():
        shoe_data = []
        for shoe in shoes:
            shoe_data.append(
                [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

        print(tabulate(shoe_data, headers=[
              "Country", "Code", "Product", "Cost", "Quantity"], tablefmt="grid"))

       # This function will iterate over the shoes list and
       # print the details of the shoes returned from the __str__
       # function. Optional: you can organize your data in a table format by using Python’s tabulate module.

    def re_stock():
        file = None
        restock_list = []
        country = []
        code = []
        product = []
        cost = []
        quantity = []
        table = []

        try:
            shoes.sort(key=lambda x: x.quantity)

            for i in range(1, 6):
                restock_list.append(shoes[i])

            print(
                "\n----------------------------Lowest stock items:----------------------------\n")

            for line in restock_list:
                country.append(line.country)
                code.append(line.code)
                product.append(line.product)
                cost.append(line.cost)
                quantity.append(line.quantity)

            table = zip(country, code, product, cost, quantity)

            print(tabulate(table, headers=('Country', 'Code', 'Product', 'Cost',
                                           'Quantity'), tablefmt='fancy_grid', showindex=range(1, 6)))
            print(
                "\n---------------------------------------------------------------------------\n")

            user_input_item = int(
                input("\nPlease confirm the index of the product you want to restock:\n"))
            user_input_qty = int(input("\nPlease confirm the new quantity:\n"))
            shoes[user_input_item].quantity = user_input_qty

            output = ''
            for item in shoes:
                output += (f'{item.country},{item.code},{item.product},{item.cost},{item.quantity}\n')

            inventory_write_test = open("inventory.txt", "w")
            inventory_write_test.write(output)
            inventory_write_test.close()

            print("\nYour product has been updated!")

        except FileNotFoundError as error:
            print("\nSorry, this file does not exist!\n")
            print(error)

        finally:
            if file is not None:
                file.close()

    # This function will find the shoe object with the lowest quantity,
    # which is the shoes that need to be re-stocked. Ask the user if they
    # want to add this quantity of shoes and then update it.
    # This quantity should be updated on the file for this shoe.

    # Define the search_shoe function within read_shoes_data

    def search_shoe(shoe_code):
        with open("inventory.txt", "r") as f:
            # Iterate over each line in the file
            for line in f:
                # Split the line into fields
                fields = line.strip().split(",")
                # Check if the shoe code matches
                if fields[1] == shoe_code:
                    # Print the matching line
                    print(line)
                    # Stop searching
                    return
            # If no shoe was found, print an error message
            print(f"No shoe with code {shoe_code} was found.")

        '''
        This function will search for a shoe from the list
        using the shoe code and return this object so that it will be printed.
        '''

    def value_per_item():
       # Get the code of the required item from the user
        item_code = input("Enter the code of the required item: ")

        # Open the file for reading
        with open('inventory.txt', 'r') as f:
            # Loop through each line of the file
            for line in f:
                # Split the line into fields
                fields = line.strip().split(',')
                # Check if the code matches the required item code
                if fields[1] == item_code:
                    # Get the cost and quantity
                    shoe_cost = float(fields[3])
                    shoe_quantity = int(fields[4])
                    # Calculate the value and print the result
                    value = shoe_cost * shoe_quantity

                    print(
                        f"The value for item with code {item_code}, {line} is: {value}")
                    break
            else:
                print(f"No item found with code {item_code}")

        '''
        This function will calculate the total value for each item.
        Please keep the formula for value in mind: value = cost * quantity.
        Print this information on the console for all the shoes.
        '''

    def highest_qty():
        # Open the file for reading
        with open('inventory.txt', 'r') as f:
            # Loop through each line of the file
            for line in f.readlines():
                # Split the line into fields
                shoe_list = line.strip().split(',')
                # Check if the code matches the required item code
                quantity = []
                for item in shoe_list:
                    quantity.append(shoe_list[4])
            max_quantity = max(quantity)
            for line in f.readlines():
                s = line.strip().split(',')
                if max_quantity in line:
                    global code
                    code = s[1]
        print(
            f"The highest quantity is: {max_quantity} for shoe with code {code} - FOR SALE!")

        '''
        Write code to determine the product with the highest quantity and
        print this shoe as being for sale.
        '''

    # ==========Main Menu=============
    '''
    Create a menu that executes each function above.
    This menu should be inside the while loop. Be creative!
    '''

    menu = (
        "===================================\n"
        "SHOE INVENTORY MANAGEMENT SYSTEM\n"
        "===================================\n"
        "1. View all shoes\n"
        "2. Add new shoe\n"
        "3. Restock shoes\n"
        "4. Search for a shoe\n"
        "5. Value per item\n"
        "6. Shoe with highest quantity\n"
        "0. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Enter your choice: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            code = input("Enter the shoe code: ")
            search_shoe(code)
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "0":
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.\n")
