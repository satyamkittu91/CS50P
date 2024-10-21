from contact import Contact
import csv
import pandas
from datetime import date
import phonenumbers
import json
import sys

today = date.today()

fields = ['Name', 'Number', 'Mail', 'Category', 'Country', 'Last Update']

#with open(r"country.txt", 'r', encoding='utf-8') as file:
#    country_dict = json.load(file)

try:
    with open(r"country.txt", 'r', encoding='utf-8') as file:
        country_dict = json.load(file)
except json.JSONDecodeError as e:
    print(f"Error loading country data: {e}")
    sys.exit()

except FileNotFoundError as e:

    sys.exit(f"\nCan't locate the 'country.txt' file\n {e}")

def add_contact(Name, Number, Mail, Category, Country):
    """
    Adds a new contact to the system. Creates a Contact object with the provided details, 
    including the current date as the 'Last Update'. This new contact is then saved 
    to the CSV file.

    Parameters:
    Name (str): The contact's name.
    Number (str): The contact's phone number.
    Mail (str): The contact's email address.
    Category (str): The category (e.g., Work, Family) for the contact.
    Country (str): The country of the contact.

    Returns:
    bool: Always returns True after successfully saving the contact.

    Example:
    >>> add_contact('John Doe', '1234567890', 'john.doe@example.com', 'Work', 'USA')
    True
    """
    last_update = today  # Capture today's date as the last update
    contact = Contact(name=Name, number=Number, mail=Mail, category=Category, country=Country, last_update=last_update)
    
    save_new(contact.to_dict())  # Save the contact as a dictionary
    return True  # Contact added successfully

def save_new(contact_dict):
    """
    Saves a new contact dictionary to the 'main.csv' file. 
    This appends the contact information as a new row in the file.

    Parameters:
    contact_dict (dict): The contact details in dictionary form.

    Returns:
    None

    Example:
    >>> save_new({'Name': 'John Doe', 'Number': '1234567890', ... })
    """
    # Read the CSV and ensure the columns are correct
    df = pandas.read_csv("main.csv")
    df.columns = fields

    new_row = pandas.DataFrame(contact_dict, index=[0])  # Convert dict to a DataFrame row
    df = pandas.concat([df, new_row], ignore_index=True)  # Append new contact
    df.to_csv("main.csv", index=False)  # Save the updated CSV

def search_contact(matches):
    """
    Displays a list of matching contacts based on a search. 
    If multiple matches are found, prompts the user to choose one.

    Parameters:
    matches (list): A list of indices where matching contacts are found.

    Returns:
    int: The index of the selected contact.
    False: If no matches are found.

    Example:
    >>> search_contact([0, 2, 4])
    2
    """
    print(f"Found {len(matches)} matching Contacts:\n")

    df = pandas.read_csv(r'main.csv')
    df.columns = fields

    # If multiple matches, let the user pick
    if len(matches) > 1:
        choice = int(input(f"Select a contact (1-{len(matches)}): ")) - 1
        return matches[choice]
    else:
        return matches[0]  # Only one match, return that index

    print("No matching contact found...")
    return False

def update_contact(index_point, update_term, new_term):
    """
    Updates a specific field for an existing contact. The contact is identified by 
    its index, and the specified field (Name, Number, Mail, Country) is updated 
    with the new value. The 'Last Update' field is also refreshed to today's date.

    Parameters:
    index_point (int): The index of the contact to be updated.
    update_term (str): The field to be updated ('name', 'number', etc.).
    new_term (str): The new value for the specified field.

    Returns:
    None

    Example:
    >>> update_contact(3, 'number', '9876543210')
    """
    df = pandas.read_csv(r'main.csv')
    df.columns = fields

    print("Old:\n")
    print(search_print_contact(index_point))  # Display the current contact before updating
    """
    response = input("You want to update this Contact? (y/n): ")
    if response.lower() in ['n', 'no']:
        exit
    elif response.lower() in ['y', 'yes']:
        # Validate the input
    """
        # Update the specific field based on the input
    if update_term.lower() == 'name':
        df.loc[index_point, 'Name'] = new_term
    elif update_term.lower() == 'number':
        if "+" in new_term:
            extracted_values = extract_country(new_term, df.loc[index_point, 'Country'])
            

            df.loc[index_point, 'Country'] = f"{extracted_values[2]}"
            df.loc[index_point, 'Number'] = extracted_values[1]

        else:
            df.loc[index_point, 'Number'] = new_term

        
    elif update_term.lower() == 'mail':
        df.loc[index_point, 'Mail'] = new_term

    elif update_term.lower() == 'country':
        for country_code, country_name in country_dict.items():
            if country_name.lower() == new_term.lower():
                country_code = country_code
                break

        df.loc[index_point, 'Country'] = f"{new_term.title()}({country_code})"

    df.loc[index_point, 'Last Update'] = today  # Set 'Last Update' to today
    df.to_csv(r'main.csv', index=False)  # Save changes back to the file
    print("New:\n")
    print(search_print_contact(index_point))

def remove_contact(index_point):
    """
    Removes a contact from the 'main.csv' file. The contact is identified by its index, 
    and the corresponding row is deleted.

    Parameters:
    index_point (int): The index of the contact to be removed.

    Returns:
    None

    Example:
    >>> remove_contact(5)
    """
    df = pandas.read_csv(r'main.csv')
    df.columns = fields

    df = df.drop(index_point)  # Remove the row at the specified index
    df.to_csv('main.csv', index=False)  # Save the file without the deleted contact

def search_print_contact(index_point):
    """
    Retrieves and returns a Contact object from the CSV file based on the index. 
    This function is useful for displaying the full details of a contact.

    Parameters:
    index_point (int): The index of the contact in the CSV file.

    Returns:
    Contact: The Contact object with all details filled.

    Example:
    >>> search_print_contact(2)
    Contact(name='John Doe', ...)
    """
    df = pandas.read_csv(r'main.csv')
    df.columns = fields

    # Extract contact details from the DataFrame
    name = df.loc[index_point, 'Name']
    number = df.loc[index_point, 'Number']
    mail = df.loc[index_point, 'Mail']
    category = df.loc[index_point, 'Category']
    country = df.loc[index_point, 'Country']
    last_update = df.loc[index_point, 'Last Update']

    # Create a Contact object to return
    contact = Contact(name=name, number=number, mail=mail,
                      category=category, country=country, last_update=last_update)
    return contact

def search_info_contact(index_point, specific_info):
    """
    Retrieves specific information (like Name, Mail, etc.) about a contact from the CSV 
    based on the provided index and information type.

    Parameters:
    index_point (int): The index of the contact in the CSV file.
    specific_info (str): The field (e.g., 'Name', 'Mail') to retrieve.

    Returns:
    str: The requested information formatted as 'Field: Value'.

    Example:
    >>> search_info_contact(3, 'name')
    'Name: John Doe'
    """
    df = pandas.read_csv(r'main.csv')
    df.columns = fields

    # Grab the specific info field and return it in a formatted string
    info = df.loc[index_point, specific_info.title()]
    return f"{specific_info.title()}: {info}"


def extract_country(number, country):
    """
    Extracts the country code from a contact number and returns the country name, the original number and 
    country code in a list form.
    """
    try:        
        if '+' in number:
            no = phonenumbers.parse(number, None)
            if country is not None:

                if country.lower() != country_dict[f"+{no.country_code}"].lower():
                    return "Mismatch Error"
                
            number_without_prefix = number.replace(f"+{no.country_code}", '')
            country_name = country_dict[f"+{no.country_code}"]
            return [f"+{no.country_code}", number_without_prefix, f"{country_name}(+{no.country_code})"]
        
        elif '+' not in number and country is not None:
            for country_code, country_name in country_dict.items():
                if country_name.lower() == country.lower():
                    return [country_code, number, f"{country_name}({country_code})"]
                
                    
        else:
            print("Invalid Number Or Country Format")
            return False
    
    except phonenumbers.NumberParseException:
        print("Invalid phone number format. Please check the number and try again")
        return False

    except KeyError:
        print("Country code not found in the database, Please check the country code and try again.")
        return False

    except IOError:
        print("Something wrong with the country database")
        return False
    
    except Exception as e:
        print(f"An unexcepted error occurred: {e}")
        return False