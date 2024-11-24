from contact import Contact
import validation
import contact_manager
import phonenumbers
import settings

import sys

def main():
    """
    The main entry point for the PeoplePal Contacts Manager Program.
    
    This function initializes the program interface and provides an interactive
    command-line interface for managing contacts. Users can perform various
    operations through simple commands:
    
    Commands:
    - add/a: Add a new contact with details like name, number, email, etc.
    - update/u: Modify existing contact information
    - remove/r: Delete a contact from the database
    - search/s: Find contacts using various search criteria
    - search_info/si: Look up specific details about a contact
    - help/h: Display detailed program instructions
    - commands/c: Show available commands
    - exit/e: Close the program
    
    The program supports features like:
    - International phone numbers with country code validation
    - Contact categorization (Work, Family, etc.)
    - Email validation
    - Fuzzy matching for category and country names
    - Default category settings
    
    Example:
    >>> main()
    *** Contacts Manager Program ***
    Type 'help/h' for instructions
    Type 'commands/c' for the list of commands
    Type 'exit/e' to quit the program
    """


    print('\n*** Contacts Manager Program ***')
    print("\nType 'help/h' for instructions\n"
          "Type 'commands/c' for the list of commands\n"
          "Type 'exit/e' to quit the program")
    
    while True:
        command = input("-> ")

        # Checking the input command and directing the user accordingly
        if command.lower() in ['command', 'c']:
            print_commands()

        elif command.lower() in ['help', 'h']:
            help()

        elif command.lower() in ['exit', 'e', '--e', 'quit', 'q', '--q']:
            sys.exit("Exiting the Program....")

        elif command == "":
            print("Command can't be empty")

        elif command.lower() in ['add', 'a']:
            add()

        elif command.lower() in ['update', 'u']:
            update()
        
        elif command.lower() in ['remove', 'r']:
            remove()

        elif command.lower() in ['search', 's']:
            search()

        elif command.lower() in ['search_info', 'si']:
            search_info()

        elif command.lower() in ['default category', 'dc']:
            setting_default_category()

def take_add_input():
    """
    Prompts the user for comprehensive contact information in an interactive way.
    
    This function collects all necessary details for creating a new contact:
    - Name: Supports both "First Last" and "Last, First" formats
    - Number: Accepts international formats with country codes
    - Mail: Validates email format
    - Category: Supports fuzzy matching with existing categories
    - Country: Optional for local numbers, required for international
    
    The function includes built-in exit points using 'exit/e' or 'cancel/c'
    at any input stage.
    
    Returns:
        tuple: (name, number, mail, category, country) containing validated input
        
    Example:
        >>> name, number, mail, category, country = take_add_input()
        Name: John Doe
        Number: +1234567890
        Mail: john@example.com
        Category: Work
        Country: USA
    """



    name = input("Name: ")
    exit_from_current_query(name)
    number = input("Number: ")
    exit_from_current_query(number)
    mail = input("Mail: ")
    exit_from_current_query(mail)
    category = input("Category: ")
    exit_from_current_query(category)
    print("Optional, if the number have country code")
    country = input("Country: ")
    exit_from_current_query(country)
    return name, number, mail, category, country

def take_update_input():
    """
    Collects information needed to update an existing contact's details.
    
    This function guides the user through the update process by:
    1. Getting a search key to find the contact
    2. Specifying which field to update (name, number, mail, etc.)
    3. Providing the new value for that field
    
    All inputs support the exit/cancel commands for user convenience.
    
    Returns:
        tuple: (search_key, update_term, new_term)
            - search_key: Term to find the contact
            - update_term: Field to be updated
            - new_term: New value for the field
            
    Example:
        >>> search_key, update_term, new_term = take_update_input()
        Search for an existing contact: John
        The term to update: number
        New Term: +1987654321
    """


    search_key = input("Search for an existing contact: ")
    exit_from_current_query(search_key)
    
    update_term = input("The term to update: ")
    exit_from_current_query(update_term)
    
    new_term = input("New Term: ")
    exit_from_current_query(new_term)

    return search_key, update_term, new_term

def take_remove_input():
    """
    Asks the user for a search key to find the contact they want to remove.

    Returns:
    str: The search key to find the contact.

    Example:
    >>> take_remove_input()
    Search Key: John
    """
    search_key = input("Search Key: ")
    exit_from_current_query(search_key)
    
    return search_key

def add():
    """
    Handles the complete contact addition process with comprehensive validation.
    
    This function:
    1. Collects contact information through take_add_input()
    2. Validates all inputs:
        - Name format and structure
        - Phone number format and uniqueness
        - Email format and uniqueness
        - Category existence/creation
        - Country code validation
    3. Extracts and validates country information from phone numbers
    4. Handles category creation for new categories
    5. Provides error handling and retry options
    
    The function maintains data integrity by checking for duplicates
    and ensures all international numbers match their country codes.
    
    Example:
        >>> add()
        Name: John Doe
        Number: +1234567890
        Mail: john@example.com
        Category: Work
        Country: USA
        New Contact added successfully
    """


    name, number, mail, categori, country = take_add_input()

    if validation.valid_name(name) == None:
        print("Name can't be None")
        resume_to_the_current_query(add, main_function=main)

    elif validation.valid_name(name) == False:
        print("Problem with the Name...")
        resume_to_the_current_query(add, main_function=main)

    else:
        name = validation.valid_name(name)
        
        if validation.valid_number(number) != False and validation.valid_number(number) != None:
            number = validation.valid_number(number)
            
            if validation.valid_mail(mail) != False and validation.valid_mail(mail) != None:
                mail = validation.valid_mail(mail=mail)
                
                category = validation.valid_category(categori)
                if category != False and category != None and category != "New" and category != FileNotFoundError:
                    

                    if validation.valid_country(country) != False and validation.valid_country(country=country) != None:
                        country = validation.valid_country(country=country)

                        

                        # Extract country code and country name
                        extracted_info = contact_manager.extract_country(number, country)
                        if extracted_info != False and extracted_info != "Mismatch Error":
                            number = extracted_info[1]
                            country = extracted_info[2]

                            if validation.valid_duplicate_number(number=number):
                                if validation.valid_duplicate_mail(mail=mail):
                                    contact_manager.add_contact(name, number, mail, category, country)
                                    print("New Contact added successfully")
                                else:
                                    print("A contact with the same mail already exists")
                                    resume_to_the_current_query(add, main)
                            else:
                                print("A contact with the same number already exists")
                                resume_to_the_current_query(add, main)
                    
                        elif extracted_info == "Mismatch Error":
                            print("Country code and Country name doesn't match...")
                            resume_to_the_current_query(add, main_function=main)
                    
                        
                        elif extracted_info == False:
                            print("Country extraction failed. Check the Phone Number or Country Name ")
                            resume_to_the_current_query(add, main_function=main)

                        else:
                            print("Unexcepted error occured, can't identify the error...")
                            resume_to_the_current_query(add, main_function=main)

                    elif validation.valid_country(country) == None:
                        if "+" in number:
                            extracted_info = contact_manager.extract_country(number, None)
                            if extracted_info != False and extracted_info != "Mismatch Error":
                                number = extracted_info[1]
                                country = extracted_info[2]

                                if validation.valid_duplicate_number(number=number) == True:
                                    if validation.valid_duplicate_mail(mail=mail) == True:
                                        contact_manager.add_contact(name, number, mail, category, country)
                                        print("New Contact added successfully")
                                    else:
                                        print("A contact with the same mail already exists")
                                        resume_to_the_current_query(add, main)
                                else:
                                    print("A contact with the same number already exists")
                                    resume_to_the_current_query(add, main)
                        
                            elif extracted_info == "Mismatch Error":
                                print("Country code and Country name doesn't match...")
                                resume_to_the_current_query(add, main_function=main)
                        
                            
                            elif extracted_info == False:
                                print("Country extraction failed. Check the Phone Number or Country Name ")
                                resume_to_the_current_query(add, main_function=main)

                            else:
                                print("Unexcepted error occured, can't identify the error...")
                                resume_to_the_current_query(add, main_function=main)

                        else:
                            print("The number doesn't have country code preifix and Country name is also not given ..."
                                  "You have to enter atleast one of them...")
                            resume_to_the_current_query(add, main_function=main)

                            
                        
                    else:
                        print("Country name Invalid...")
                        resume_to_the_current_query(add, main_function=main)

                elif category == "New":
                    print("This group of category doesn't exist...")
                    create_new_y_or_n = input("Create a New Category, Y/N: ")
                    if create_new_y_or_n.lower() in ['yes', 'y']:
                        if settings.create_new_category(categori.title()) == True:
                            print("New Category Created, Successfully")
                            resume_to_the_current_query(add, main_function=main)
                        else:
                            print("Error while creating new category...")
                            resume_to_the_current_query(add, main_function=main)

                    if create_new_y_or_n.lower() in ['no', 'n']:
                        print("You have to enter the category of the contact...")
                        resume_to_the_current_query(add, main_function=main)

                elif category == None:
                    print("You must enter the category of the contact...")
                    resume_to_the_current_query(add, main_function=main)


            else:
                print("Problem with the Mail...")
                resume_to_the_current_query(add, main_function=main)

        elif validation.valid_number(number) == None:
            print("Number can't be None")
            resume_to_the_current_query(add, main_function=main)
        else:
            print("Problem with the Number...")
            resume_to_the_current_query(add, main_function=main)

def update():
    """
    Manages the complete contact update workflow with validation.
    
    Features:
    - Fuzzy searching for finding contacts
    - Field-specific validation for updates
    - Automatic country code updating when phone numbers change
    - Duplicate checking for emails and phone numbers
    - Last update timestamp maintenance
    
    The function prevents invalid updates and maintains data consistency
    by validating all changes before committing them.
    
    Example:
        >>> update()
        Search for an existing contact: John
        The term to update: number
        New Term: +1987654321
        [Shows old and new contact details]
    """

    search_key, update_term, new_term = take_update_input()
    if validation.valid_exist(search_key) != False:
        index_point = contact_manager.search_contact(validation.valid_exist(search_key))
        if validation.valid_term(new_term) != False:
            if validation.valid_duplicate_number(number=new_term) == True:
                if validation.valid_duplicate_mail(mail=new_term) == True:
                    contact_manager.update_contact(index_point, update_term, validation.valid_term(new_term)[1])
                else:
                    print("A contact with the same mail already exists")
                    resume_to_the_current_query(update, main)
            else:
                print("A contact with the same number already exists")
                resume_to_the_current_query(update, main)

        else:
            print("Problem with the new Term...")
            resume_to_the_current_query(update, main)
    else:
        print("Contact with the given info doesn't exist...")
        resume_to_the_current_query(current_function=update, main_function = main)

def remove():
    """
    Removes a contact from the system based on a search key. 
    If a match is found, it asks for confirmation before deleting the contact.
    
    Example:
    >>> remove()
    """
    search_key = take_remove_input()
    if validation.valid_exist(search_key) != False:
        index_point = contact_manager.search_contact(validation.valid_exist(search_key))
        Verification = input("Are you sure you wanna delete this contact, Y/N: ")

        if Verification in ['yes', 'y', 'Y']:
            contact_manager.remove_contact(index_point)
        else:
            main()
    else:
        print("Contact with the given info doesn't exist...")
        resume_to_the_current_query(remove, main_function=main)

def search():
    """
    Allows the user to search for contacts in the system. 
    If a match is found, the contact's details are displayed.
    
    Example:
    >>> search()
    """
    search_key = input("Search Key: ")
    matches = validation.valid_exist(search_key)
    if matches != False:
        index_point = contact_manager.search_contact(matches)
        print(contact_manager.search_print_contact(index_point))

def search_info():
    """
    Allows the user to search for a specific piece of information about a contact.
    
    Example:
    >>> search_info()
    """
    search_key = input("Search Key: ")
    exit_from_current_query(search_key)
    if validation.valid_exist(search_key) != False:
        index_point = contact_manager.search_contact(validation.valid_exist(search_key))
        specific_info = input("Specific info of the contact: ")
        print(contact_manager.search_info_contact(index_point, specific_info))
    else:
        print("Contact with the given info doesn't exist...")
        resume_to_the_current_query = input("Resume to the current query, Y/N: ")
        if resume_to_the_current_query in ['yes', 'y', 'Y']:
            search_info()
        else:
            main()


def setting_default_category():
    default_category = input("Set this category to default: ")
    exit_from_current_query(default_category)
    category = validation.valid_category(default_category)
    if category != False and category != None and category != "New":
        if settings.set_default_category(category) == False:
            print("Error while setting default category...")

        else:
            print(f"{category} set as default category successfully...")

    elif category == "":
        print("category can't be none")
        resume_to_the_current_query(setting_default_category, main)

    else:
        print("Category doesn't exist...")
        resume_to_the_current_query(setting_default_category, main)

def resume_to_the_current_query(current_function, main_function):
    user_input = input("Resume the current query, Y/N: ")
    if user_input.lower() in ['yes', 'y']:
        current_function()
    elif user_input.lower() in ['no', 'n']:
        main_function()
    else:
        print("Invalid Input..."
              "You have to enter only Y or N...")
        resume_to_the_current_query(current_function, main_function)

def exit_from_current_query(vari):
    if vari.lower() in ["exit", "e", "--e", "quit", "q", "--q"]:
        sys.exit()
    elif vari.lower() in ["Cancel", "c", "--c"]:
        main()
    else:
        None

def print_commands():
    """
    Displays the list of available commands and their descriptions.
    This function provides a comprehensive guide to interacting with the contact manager.
    """
    commands = {
        "1": "Add a new contact",
        "2": "Search for a contact",
        "3": "Update an existing contact",
        "4": "Remove a contact",
        "5": "View all contacts",
        "6": "Create a new category",
        "7": "Set a default category",
        "8": "Exit the program"
    }

    print("\nAvailable Commands:")
    for key, description in commands.items():
        print(f"  {key}. {description}")

    print("\nFor detailed help on a specific command, use the 'help' function.\n")


def help(command=None):
    """
    Provides detailed help for a specific command or general guidance.
    
    Parameters:
        command (str): The specific command to get help for. If None, provides general help.
    """
    help_text = {
        "1": """
        Add a New Contact:
        - Adds a contact to the system with details like Name, Number, Email, Category, and Country.
        - Example:
          Enter 'Name': John Doe
          Enter 'Number': +1234567890
          Enter 'Mail': john.doe@example.com
          Enter 'Category': Work
          Enter 'Country': USA
        """,
        "2": """
        Search for a Contact:
        - Finds contacts by name or other details.
        - Displays matching contacts and allows selecting one for further actions.
        - Example: Enter 'John' to find all contacts containing 'John'.
        """,
        "3": """
        Update an Existing Contact:
        - Allows updating a specific field of a contact (Name, Number, Mail, Category, or Country).
        - Example: Update John's number to '+9876543210'.
        """,
        "4": """
        Remove a Contact:
        - Deletes a contact from the system.
        - Example: Select a contact index to remove it permanently.
        """,
        "5": """
        View All Contacts:
        - Displays all saved contacts in a tabular format.
        - Example: Use this command to review your contact list.
        """,
        "6": """
        Create a New Category:
        - Adds a new category to the system.
        - Example: Create a 'Colleagues' category for work-related contacts.
        """,
        "7": """
        Set a Default Category:
        - Sets a specific category as the default for new contacts.
        - Example: Set 'Family' as the default category.
        """,
        "8": """
        Exit the Program:
        - Safely exits the application and saves all changes.
        """
    }

    if command and command in help_text:
        print(f"\nHelp for Command {command}:")
        print(help_text[command])
    else:
        print("\nGeneral Help:")
        print("This contact management system allows you to manage and organize your contacts efficiently.")
        print("Use the 'print_commands' function to see all available commands.")
        print("For help with a specific command, use 'help(<command_number>)'.")


if __name__ == "__main__":
    main()
