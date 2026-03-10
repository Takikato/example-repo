from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def get_cost(self):

        # returns the cost of the object
        return f"\nThe cost is:{self.cost}\n"


    def get_quantity(self):

        # returns the quantity of the object
        return f"\nThe quantity is {self.quantity}\n"


    def __str__(self):

        # put all the information I want to print in a variable to make
        # it easier to edit and to understand
        final_string = (
            "\n ===INFORMATION=== \n"
            f"The country the product is from: {self.country}\n"
            f"The product code is: {self.code}\n"
            f"The product name is: {self.product}\n"
            f"The cost of the product is: {self.cost}\n"
            f"The quantity of the product is: {self.quantity}\n"
                        )

        return final_string



#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoes_list =[]

# stores a list of nun object shoes
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object
    with this data and append this object into the shoes list.
    One line in this file represents data to create one object of shoes.
    '''
    try:
        with open("inventory.txt", "r", encoding="utf-8") as file:
            next(file)  # starts reading the file on the second line

            # loops through all the lines in the file being read
            for i in file:
                # strips the file lines if there were accidental spaces and
                # splits the line so that it can be used in variable
                # "object_create"
                list_split = i.strip().split(",")

                # stores none object information so that it can be used in
                # functions such as the view_all function that requires a none
                # object list to work
                shoe_list.append(list_split)

                # uses the splitted information in the variables above to
                # create a Shoe object by using the unpacked information
                object_create = Shoe(*list_split)

                # adds all the new objects to the shoes_list variable
                shoes_list.append(object_create)

    except FileNotFoundError:
        print("inventory.txt was not found on your device, please make "
            "sure that you have this file on your device before running "
            "the program.")



def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    print("\n ===CAPTURE SHOE===\n")

    # different variables that ask for the user input to build the new object
    country = input("please enter the country here: ")

    code = input("Please enter the code here: ")

    product = input("please enter the product here: ")

    # create a function that will return a number for the variables,
    # item will be the variable that the user will need to enter
    def int_function(item):

        while True:

            try:
                # saves the number the user enter in value
                value = int(input(f"Please enter the {item} here: "))

                # the return replaces the break and will return the number
                return value


            except ValueError:
                print("That is not a number.")


    cost = int_function("cost")

    quantity = int_function("quantity")

    # uses all the user inputs to build the object
    new_shoe = Shoe(country, code, product, cost, quantity)

    new = [country, code, product, cost, quantity]

    # variable that hold all the info for the new line
    print_text = country, code, product, cost, quantity

    # confirms that the new product has been added to the user
    print(f"\n{print_text} has been added to the list")

    # stores the new object in the new_shoe list
    shoes_list.append(new_shoe)

    # appends the new variable for the view_all variable
    shoe_list.append(new)

    # open the "inventory.txt" and adds in new information in it
    with open("inventory.txt", "a", encoding="utf-8") as file:

        # adds the new line to the txt file
        file.write(f"\n{country},{code},{product},{cost},{quantity}")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

    print("\n ===All PRODUCTS===\n")

    # create a variable to store all the headers for the tabulate function
    headers = ["country", "code","product", "cost", "quantity"]

    # prints out a table to display all the information and different shoes
    # in a neat table and makes it easy for the user to read
    print(tabulate(shoe_list, headers = headers, tablefmt = "fancy_grid"))


def re_stock():

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. It will also ask the ask
    the user if they want to add this quantity of shoes and then update it.
    '''

    print("\n ===RESTOCKING===\n")

    # different variables for all the loops and functions below
    # default quantity added
    add_quantity = 5

    # variable that stores the lowest index
    lowest_index = None

    # variable that stores the lowest quantity
    lowest_quantity = float("inf")

    # variable that stores the lowest line of information in the file
    lowest_line = None

    # variable that helps to detect if the user want to add a different value
    quantity_change = False


    # open and reads the file "inventory.txt"
    with open("inventory.txt", "r", encoding="utf-8") as file:

        next(file)   # starts reading the file on the second line

        # stores all the lines that were read in the file in this variable
        lines = file.readlines()

    # a loop that goes through each line of information
    for i, line in enumerate(lines):

        # variable that stores the different information in each of its
        # own variables
        country, code, product, cost, quantity = line.strip().split(",")

        # change the quantity variable into a integer so that it does
        # not cause errors
        quantity = int(quantity)

        # if statement that look for the line with the smallest quantity
        if quantity < lowest_quantity:

            # stores lowest quantity
            lowest_quantity = quantity

            # stores lowest index
            lowest_index = i

            # stores lowest line by adding all the different
            # variables together to form a line again
            lowest_line = (country, code, product, cost, quantity)

    # prints out the lowest line so that the user knows what is the product
    # with the lowest stock and how much stock it haas
    print(
        f"\n{lowest_line} is the product with "
        f"the lowest stock of {lowest_quantity}"
        )

    # loop that does not stop until the user enters the necessary inputs
    while True:

        print(f"\nThe default quantity added is {add_quantity}.")

        # put the text into a variable so that everything will fit
        user_text = ("Would you like to keep it that way Yes or No?: ")

        # print instructions for the user
        user_input = input(user_text)

        # strips and lowers the user input to avoid any future errors
        user_input.strip().lower()

        # if statement that checks if the user enter yes or no
        if user_input == "yes" or user_input == "no":

            # if statement that executes when used typed "no"
            if user_input == "no":

                # changes the variables for False to True and stops loop
                quantity_change = True
                break

            elif user_input == "yes":

                # changes the variables for False to True and stops loop
                quantity_change = True
                break

            else:
                print("That is not a valid input.")


    # if statement that executes if the user wants to change the quantity
    # that is going to be added to the stock
    if quantity_change == True:

        # loop that does not stop until the user enters the necessary inputs
        while True:


            try:

                # asks the user what the value of the added stock should be
                user_input = int(input("How much would you like to add?: "))

                # changes the default value into users value
                add_quantity = user_input
                break

            except ValueError:
                print("That is not a valid input.") # error message for user

    # if statement that runs if the lowest_index is not None
    if lowest_index is not None:

        # put back all the values back in their variables
        country, code, product, cost, quantity = lowest_line

        # create the variable that will store the new stock
        new_quantity = int(quantity) + add_quantity

        # put the line that will be changed in a variables so that it will fit
        lines_f = (f"{country},{code},{product},{cost},{new_quantity}\n")

        # variable that holds the new restocked line
        lines[lowest_index] = lines_f

        # prints text that tells the user what item has been restocked
        print(f"\n{product} from {country} has been restocked. "
            f"Total stock is now equal to {new_quantity}")

    # open the "inventory.txt" and writes information in it
    with open("inventory.txt", "w", encoding="utf-8") as file:

        # puts the header of the document back
        file.write("Country,Code,Product,Cost,Quantity\n")

        # writes down the line that was restocked and updates it
        file.writelines(lines)


def search_shoe():

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    print("\n ===SHOE SEARCH===\n")

    code_line = None

    # open and reads the file "inventory.txt"
    with open("inventory.txt", "r", encoding="utf-8") as file:

        next(file)   # starts reading the file on the second line

        # stores all the lines that were read in the file in this variable
        lines = file.readlines()


    while True:

        # variables that will be used to break the loop
        breaker = False

        # variables that stores the users input
        user_input = input("\nplease enter the product code here: ")

        # create variable to save the line that the user is looking for


        # a loop that goes through each line of information
        for i, line in enumerate(lines):

            # variable that stores the different information in each of its
            # own variables
            country, code, product, cost, quantity = line.strip().split(",")

            # if statement that looks if the code the user entered exists
            if user_input == code:

                # stores the line the user it looking for
                code_line = (f"\n{country},{code},{product},"
                             f"{cost},{quantity}\n")

                # turn the breaker true so that it breaks the loop
                breaker = True
                break

        # breaks loop if the breaker is true
        if breaker == True:
            break

        # prints error message that the code does not exists in the list
        print(f"\n{user_input} does not exist, please try again.\n")

    # returns the line that the user is looking for
    print(code_line)


def value_per_item():

    '''
    This function will calculate the total value for each item.
    '''

    print("\n ===ALL PRODUCT VALUE===\n")

    # create a variable to store all the headers for the tabulate function
    headers = ["country", "code","product", "value"]

    # create a empty list which will store all the information for the table
    calculation = []

    # a loop that will create the lines that we need for the table
    for country, code, product, cost, quantity in shoe_list:

        # change the quantity to a int to avoid errors iin calculations
        quantity = int(quantity)

        # change the cost to a int to avoid errors iin calculations
        cost = int(cost)

        # times cost and quantity to get the value of the product
        value = (quantity * cost)

        # append all the new lists into a list to be used for the table
        calculation.append([country, code, product, value])

    # prints out a table to display all the product values
    # in a neat table and makes it easy for the user to read
    print(tabulate(calculation, headers = headers, tablefmt = "fancy_grid"))


def highest_qty():

    '''
    This function will look for the product with the most quantity and
    print the product out as being for sale
    '''

    print("\n ===PRODUCT WITH HIGHEST QUANTITY===\n")

    # reads the txt sho that we can use the shoe_list variable
    read_shoes_data()

    # creates a empty list where the line with the most quantity will be
    max_product = []

    # creates a variable with -1 so that it will always be smaller than
    max_quantity = -1

    # creates a loop that unpacks the shoe_list variable
    for country, code, product, cost, quantity in shoe_list:

        # turn quantity into a integer to avoid calculation errors
        quantity = int(quantity)

        # an if statement that looks for the line with the highest quantity
        if quantity > max_quantity:

            # saves the line with the highest quantity
            max_product = country, code, product, cost, quantity

            # saves the quantity of the highest quantity line
            max_quantity = quantity


    # stores the text that will be printed for the user
    # {max_product[2]} is the products name and
    # {max_product[3]} is how much the product costs
    user_print = (f"{max_product[2]} costs R{max_product[3]}")

    # prints the user the the product with the highest quantity thats for sale
    print(user_print)

#==========Main Menu=============
'''
This wil be the menu the user will see and will use to execute all the
functions available in the list
'''

# dictionary that will display all the options the user will have
menu_dic = {
    1 : "Add a new shoe to the stock",
    2 : "View all shoes",
    3 : "Restock the lowest shoes in stock",
    4 : "Search for shoes",
    5 : "See the Value of all the Shoes",
    6 : "The shoes with the highest quantity",
    7 : "EXIT program"
}

# runs the read_shoes_data function once
read_shoes_data()

# loop that does not stop until the user wants to exit program
while True:

    print("\n ===Menu===\n")

    # variable that stores text that will be printed to user
    user_text = ("\nPlease enter the number of the"
                        " action you want to do here: ")

    # loop that does not stop until user entered a valid number
    while True:

        try:

            # prints out all the options for the user
            for i, text in menu_dic.items():
                print(f"{i}. {text}")

            # asks user for a number
            menu_input = int(input(user_text))

            # is user entered correct number it breaks loop
            if 1 <= menu_input <= 7:

                break

            # if user entered incorrect number it will display error
            else:
                print(f"\n{menu_input} is not a valid input, "
                  "please enter only a number that is from the menu.")

            # allows user to read what is being sed before going back
            return_menu = input("\nPress Enter when you are "
                            "ready to go back to menu")


        except ValueError:

            print("\nThat is not a valid input, "
                  "please enter only a number that is from the menu.")

            # allows user to read what is being sed before going back
            return_menu = input("\nPress Enter when you are "
                            "ready to go back to menu")



    # if user enters 1 then runs capture_shoes function
    if menu_input == 1:
        capture_shoes()

        # allows user to read what is being sed before going back
        return_menu = input("\nPress Enter when you are "
                            "ready to go back to menu")

    # if user enters 2 then runs view_all function
    elif menu_input == 2:
        view_all()

        # allows user to read what is being sed before going back
        return_menu = input("\nPress Enter when you are "
                            "ready to go back to menu")

    # if user enters 3 then runs re_stock function
    elif menu_input == 3:

        re_stock()

        # allows user to read what is being sed before going back
        return_menu = input("\nPress Enter when you are "
                            "ready to go back to menu")

    # if user enters 4 then runs search_shoe function
    elif menu_input == 4:

        search_shoe()

        # allows user to read what is being sed before going back
        return_menu = input("\nPress Enter when you are "
                            "ready to go back to menu")

    # if user enters 5 then runs value_per_item function
    elif menu_input == 5:
        value_per_item()

        # allows user to read what is being sed before going back
        return_menu = input("\nPress Enter when you are "
                            "ready to go back to menu")

    # if user enters 6 then runs highest_qty function
    elif menu_input == 6:

        highest_qty()

        # allows user to read what is being sed before going back
        return_menu = input("\nPress Enter when you are "
                            "ready to go back to menu")


    # if user enters 7 it will stop program
    elif menu_input == 7:

        print("\nGood bye")

        break
