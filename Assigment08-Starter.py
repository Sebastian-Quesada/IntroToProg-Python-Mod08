# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# SQuesada,12.5.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #

# Name of file to open or create
strFileName = 'Prods.txt'
lstOfProductsObjects = []

class Products:
    """Stores data about a product:
    properties:
        prod_name: (string) with the products's  name
        prod_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SQuesada,12.08.19,Modified code to complete assignment 8
    """
    # ********Constructor******** #
    #Constructor to set the name and cost of the product
    def __init__(self, Products_name: str, Products_cost: float):
        # ******** Attributes START ******** #
        try:
            self.__Products_name = str(Products_name)
            self.__Products_cost = float(Products_cost)
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))
        # ******** Attributes END ******** #

    # ********Properties START******** #
    @property
    # Property Getter
    def Products_name(self):
        return str(self.__Products_name)

    @Products_name.setter
    #Property Setter
    def Products_name(self, value: str):
        if str(value).isnumeric():
            self.__Products_name = value
        else:
            raise Exception("Sorry, names can not be Numbers! ")
        #Error because the input  has to be a string

    # Product price (as a number)
    @property
    #Cost Getter
    def Products_cost(self):
        return float(self.__Products_cost)
    #Float

    @Products_cost.setter
    #Cost Setter
    def Products_cost(self, value: float):
        if str(value).isnumeric():
            self.__Products_cost = float(value)
        # cast to float
        else:
            raise Exception("Error: The Cost must be entered as Number.")

    # ********Methods******** #
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.Products_name + "," + str(self.Products_cost)
    # ********Methods******** #

    # ********Properties END******** #

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SQuesada,12.19.2019,Modified code to complete assignment 8"""

    @staticmethod
    #Method to save data to file
    def save_data_to_file(file_name: str, list_of_Products_objects: list):
        success_status = False
        try:
            file = open(file_name, "w+")
            #Will create the file if not created
            for Products in list_of_Products_objects:
                file.write(Products.__str__() + "\n")
            file.close()
            #closing the file
            success_status = True
            #Changing file to boolean
        except Exception as e:
            print("There was a Error! Please review.")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):

        """ Reads data from a file into a list of product rows
        :param file_name: (string) with name of file
        :return: (list) of product rows """
        list_of_Products_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Products(data[0], data[1])
                list_of_Products_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_Products_rows


# *************Processing************* #


# *************Presentation (Input/Output)************* #
class IO:
    """ A class for performing Input and Output methods:
    # print_menu_items():
    # print_current_list_items(list_of_rows):
    # input_product_data(): changelog: (When,Who,What) RRoot,1.1.2030,Created Class: """

    @staticmethod
    #Method to print menu
    def print_menu():
        """ Print a menu of choices to the user """
        print()
        print()
        print(''' Menu:  
            1) Show current data. 
            2) Add a new item. 
            3) Save Data to a File. 
            4) Exit the Program ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
            :return: string """
        choice = str(input("Please make a selection: [1 to 4] - ")).strip()
        print()
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of rows
            :param list_of_rows: (list) of rows you want to display """
        print("******* The current items Products are: *******")
        for row in list_of_rows:
            print("Name: " + row.Products_name + " Cost: " + "$" + str(row.Products_cost))
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_Products_data():
        """ Gets data for a product object
            :return: (Product) object with input data """
        try:
            name = str(input("What is the name of the Product? - ").strip())
            cost = float(input("What is the cost of the Product? - ").strip())
            print()  # Add an extra line for looks
            p = Products(Products_name=name, Products_cost=cost)
        except Exception as e:
            print(e)
        return p


# *************Presentation (Input/Output)************* #


# *************Main Body of Script*************  ---------------------------------------------------- #
try:
    lstOfProductsuctsObjects = FileProcessor.read_data_from_file(strFileName)

    while True:  # Show user a menu of options
        IO.print_menu()
        # Get user's menu option choice
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':
            # Show user current data
            IO.print_current_list_items(lstOfProductsObjects)
            continue
        elif strChoice.strip() == '2':
            # Let user add data
            lstOfProductsObjects.append(IO.input_Products_data())
            continue
        elif strChoice.strip() == '3':
            # let user save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, lstOfProductsObjects)
            continue
        elif strChoice.strip() == '4':
            break
except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')


# Main Body of Script  ---------------------------------------------------- #
