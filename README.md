#Shoe Inventory System

----------------------------------------------------------

This is a simple shoe inventory system that allows you to capture, read, view, and restock shoes.

####The Shoe class is used to define the Shoe object with the following attributes:

country
code
product
cost
quantity
The system reads the data from the inventory.txt file to create the shoe objects.

Usage
The following are the functions provided by the system:

read_shoes_data(): This function opens the inventory.txt file and reads the data from this file. It then creates Shoe objects with this data and appends these objects to the shoes list. Each line in the file represents data to create one object of Shoe. Use the try-except in this function for error handling.

capture_shoes(): This function allows a user to capture data about a shoe and use this data to create a Shoe object and append this object to the shoes list. It also writes the shoe data to the inventory.txt file.

view_all(): This function iterates over the shoes list and prints the details of the shoes returned from the __str__ function. It also organizes the data in a table format by using Python’s tabulate module.

re_stock(): This function identifies the lowest stock items in the shoes list and prints a report with these items' details.

Running the System
To run the system, simply run the inventory.py file.

When the system starts, you will be presented with the following options:
1. Read shoes data
2. Capture shoes
3. View all shoes
4. Re-stock
5. Quit

Dependencies
The system uses the tabulate module for pretty printing. You can install this module by running the following command:
pip install tabulate
