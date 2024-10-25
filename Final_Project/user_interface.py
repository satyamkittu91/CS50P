from contact import Contact
import validation
import contact_manager
import phonenumbers
import settings

import sys

def main():
    """
    The main function that starts the Contacts Manager Program.
    Displays helpful instructions and waits for user commands 
    like 'add', 'update', 'remove', and 'search'. Type 'exit' to quit the program.
    
    This is where the contact magic happens!
    
    Example:
    >>> main()
    *** Contacts Manager Program ***
    Type 'help/h' for instructions
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
    Prompts the user for contact details like name, number, mail, category, and country.
    
    Returns:
    tuple: Contains name, number, mail, category, and country entered by the user.
    
    Example:
    >>> take_add_input()
    Name: John Doe
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
    Asks the user for inputs needed to update a contact: 
    a search key, the term to update, and the new value.

    Returns:
    tuple: The search key, the field to update, and the new value.

    Example:
    >>> take_update_input()
    Search for an existing contact: John
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
    Handles the process of adding a new contact. 
    Takes inputs from the user, validates them, and adds the contact if all inputs are valid.
    
    If a validation fails, it gives the user an option to retry or go back to the main menu.
    
    Example:
    >>> add()
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

                            if validation.valid_duplicate_name(name=name):
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
                            else:
                                print("A contact with the same name already exists")
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

                                if validation.valid_duplicate_name(name=name) == True:
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
                                else:
                                    print("A contact with the same name already exists")
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
    Handles updating an existing contact. 
    The user is prompted to search for the contact they want to update, 
    select the field to update, and provide the new value.
    
    If no matching contact is found, the user can retry or return to the main menu.
    
    Example:
    >>> update()
    """
    search_key, update_term, new_term = take_update_input()
    if validation.valid_exist(search_key) != False:
        index_point = contact_manager.search_contact(validation.valid_exist(search_key))
        if validation.valid_term(new_term) != False:

            contact_manager.update_contact(index_point, update_term, validation.valid_term(new_term)[1])

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
    Prints the available commands for the user to interact with the system.
    
    Example:
    >>> print_commands()
    Commands:
    add/a : To add a new Contact to Database.
    """
    commands = {
        'add/a': 'To add a new Contact to Database.',
        'update/u': 'To update an existing Contact in Database.',
        'remove/r': 'To remove an existing Contact in Database.',
        'search/s': 'To search for an existing Contact in Database.',
        'search_info/si': 'To search for a specific info about an existing contact.',
        'exit/e': 'To EXIT from the program.'
    }
    print("Commands:")
    for key, value in commands.items():
        print(f"{key} : {value}")

def help():
    """
    Provides detailed help and instructions on how to use the Contacts Manager Program.
    This function explains each command and its purpose, guiding the user on how to manage their contacts efficiently.
    """
    help_text = """
    *** Welcome to the Contacts Manager Program Help Center! ***
    
    This program helps you organize and manage your contacts with ease. 
    Below is a quick guide to help you get started:

    Basic Commands:
    ---------------
    1. 'add' or 'a': 
       - Use this command to add a new contact. You’ll be asked to provide the contact's Name, Number, Email, Category (like Work, Family, etc.), and Country. 
       - The contact will be validated and saved if all inputs are correct.
    
    2. 'update' or 'u': 
       - Use this command to update any existing contact. 
       - You'll be prompted to search for the contact first, choose what information you want to update (like name, number, etc.), and provide the new value.
    
    3. 'remove' or 'r': 
       - Use this command to remove a contact from your database. 
       - After confirming, the selected contact will be permanently deleted.

    4. 'search' or 's': 
       - Use this command to search for a contact by their name, number, or other details. 
       - It will display the matching contacts for you to select from.
    
    5. 'search_info' or 'si': 
       - If you want specific information about a contact (like just their email or category), use this command. 
       - You'll search for the contact first, then choose which specific detail you want to see.

    6. 'commands' or 'c': 
       - This command shows the list of all available commands, in case you need a quick reference.

    7. 'exit' or 'e': 
       - Type this to exit the program. All your changes will be saved before exiting.

    Extra Tips:
    -----------
    - The program will always validate your input (name, number, email, etc.), so don’t worry about making small mistakes! 
    - If you ever run into trouble or an input doesn't seem to work, the program will guide you back to the main menu or allow you to retry the process.
    - Feel free to explore the commands, and don’t hesitate to add, update, or remove contacts as needed. It's your personal contact organizer!

    We hope you find this program helpful in managing your contacts. 
    If you ever need a refresher, just type 'help' or 'h' at any time!

    Enjoy managing your contacts!
    """
    print(help_text)


if __name__ == "__main__":
    main()
