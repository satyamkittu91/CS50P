from contact import Contact
import validation
import contact_manager

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
          "Type 'commands/c' for command list\n"
          "Type 'exit/e' to quit the program")
    
    while True:
        command = input("-> ")

        # Checking the input command and directing the user accordingly
        if command in ['command', 'c']:
            print_commands()

        elif command in ['help', 'h']:
            help()

        elif command in ['exit', 'e', '--e', 'quit', 'q', '--q']:
            sys.exit("Exiting the Program....")

        elif command == None:
            print("Command can't be empty")

        elif command in ['add', 'a']:
            add()

        elif command in ['update', 'u']:
            update()
        
        elif command in ['remove', 'r']:
            remove()

        elif command in ['search', 's']:
            search()

        elif command in ['search_info', 'si']:
            search_info()

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
    number = input("Number: ")
    mail = input("Mail: ")
    category = input("Category: ")
    country = input("Country: ")

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
    update_term = input("The term to update: ")
    new_term = input("New Term: ")

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
    
    return search_key

def add():
    """
    Handles the process of adding a new contact. 
    Takes inputs from the user, validates them, and adds the contact if all inputs are valid.
    
    If a validation fails, it gives the user an option to retry or go back to the main menu.
    
    Example:
    >>> add()
    """
    name, number, mail, category, country = take_add_input()

    if validation.valid_name(name) == None:
        print("Name can't be None")
        resume_the_current_query = input("Resume the current query, Y/N: ")
        if resume_the_current_query in ['yes', 'y', 'Y']:
            add()
        else:
            main()

    elif validation.valid_name(name) == False:
        print("Problem with the Name...")
        resume_the_current_query = input("Resume the current query, Y/N: ")
        if resume_the_current_query in ['yes', 'y', 'Y']:
            add()
        else:
            main()

    else:
        name = validation.valid_name(name)
        if validation.valid_number(number) != False:
            if validation.valid_mail(mail):
                if validation.valid_category(category):
                    if validation.valid_country(country) != False:
                        contact_manager.add_contact(name, validation.valid_number(number), mail, category, country.title())
                    else:
                        print("Country name Invalid...")
                else:
                    print("This group of category doesn't exist...")
            else:
                print("Problem with the Mail...")
                resume_the_current_query = input("Resume the current query, Y/N: ")
                if resume_the_current_query in ['yes', 'y', 'Y']:
                    add()
                else:
                    main()
        else:
            print("Problem with the Number...")
            resume_the_current_query = input("Resume the current query, Y/N: ")
            if resume_the_current_query in ['yes', 'y', 'Y']:
                add()
            else:
                main()

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
        contact_manager.update_contact(index_point, update_term, new_term)
    else:
        print("Contact with the given info doesn't exist...")
        resume_to_the_current_query = input("Resume to the current query, Y/N: ")
        if resume_to_the_current_query in ['yes', 'y', 'Y']:
            update()
        else:
            main()

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
        resume_to_the_current_query = input("Resume to the current query, Y/N: ")
        if resume_to_the_current_query in ['yes', 'y', 'Y']:
            remove()
        else:
            main()

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
