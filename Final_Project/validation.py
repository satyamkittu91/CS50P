import re
import pandas
import pycountry

def valid_name(name):
    """
    Validate and format a name. If the name starts with an alphabetic character, 
    it processes the name. If the name contains a comma (like 'Last, First'), 
    it flips it to 'First Last' format and capitalizes both. Otherwise, 
    it returns the title-cased version of the name. 

    Parameters:
    name (str): The name to be validated and formatted.

    Returns:
    str: The formatted name if valid.
    None: If the name is None or empty.
    False: If the name doesn't start with a letter.

    Example:
    >>> valid_name('Doe, John')
    'John Doe'
    """
    if name == None or name == '':  # Check if the name is empty or None
        return None
    if name[0].isalpha():  # Make sure the name starts with a letter
        if ',' in name:
            last, first = name.split(', ')
            name = f"{first.strip()} {last.strip()}"  # Flip 'Last, First' to 'First Last'
            return name.title()  # Return a pretty version with capitalized words
        
        return name.title()  # Simple name with capitalization
    else:
        return False  # Nope, that’s not a valid name
    
def valid_number(number):
    """
    Validates a phone number by removing spaces, parentheses, and dashes. 
    Accepts numbers with a length of 10 to 15 digits, optionally with a '+' prefix.

    Parameters:
    number (str): The phone number to be validated.

    Returns:
    str: The cleaned number if valid.
    None: If the number is None or empty.
    False: If the number format is invalid.

    Example:
    >>> valid_number('+123 456 7890')
    '+1234567890'
    """
    if not number:  # Empty number? No validation needed then
        return None
    
    number = re.sub(r'[\s()-]', '', number)  # Clean out all the fluff
    if re.match(r"^\+?\d{10,15}$", number):  # Check for valid phone number format
        try:
            return f'{number}'  # Return the string format number (nice and clean)
        except ValueError:
            return False  # Something went wrong (though it shouldn’t)
    else:
        return False  # Invalid number format

def valid_mail(mail):
    """
    Validates an email address based on a fairly permissive regex. 
    Makes sure the email is properly structured.

    Parameters:
    mail (str): The email address to be validated.

    Returns:
    str: The validated email if it's in the correct format.
    None: If the email is None or empty.
    False: If the email format is invalid.

    Example:
    >>> valid_mail('user@example.com')
    'user@example.com'
    """
    if not mail:  # No email? No problem, just say it's invalid
        return None

    # Match the email to see if it's valid
    if valid := re.match(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", mail):
        return mail  # Email looks good, return it
    
    else:
        return False  # Nope, not a valid email address

VALID_CATEGORIES = ['Friends', 'Work', 'Family', 'Acquaintances', 'Other', 'Test']

def valid_category(category):
    """
    Validates if a category exists within the predefined list of categories. 
    Categories are title-cased before comparison.

    Parameters:
    category (str): The category to be validated.

    Returns:
    str: The title-cased category if valid.
    False: If the category is not in the list.

    Example:
    >>> valid_category('friends')
    'Friends'
    """
    if category.title() in VALID_CATEGORIES:  # Match category ignoring case
        return category.title()  # Return a nice title-cased category
    else:
        return False  # That's not a valid category, sorry

def valid_country(country):
    """
    Validates if the given country name exists using pycountry library.
    A country lookup will attempt to find the full, proper name.

    Parameters:
    country (str): The country name to be validated.

    Returns:
    str: The full name of the country if valid.
    False: If the country cannot be found.

    Example:
    >>> valid_country('IN')
    'India'
    """
    try:
        # Look up the country using pycountry
        country_data = pycountry.countries.lookup(country)
        return country_data.name  # Return the official name of the country
    except LookupError:
        return False  # Oops, couldn't find that country

def valid_exist(search_key):
    """
    Checks if a search key exists in the 'main.csv' file. 
    It will search through the 'Name', 'Number', and 'Mail' fields, 
    returning the index of any matches.

    Parameters:
    search_key (str): The search term used to find matches in the CSV.

    Returns:
    list: A list of row indices where the match occurs.
    False: If no match is found.

    Example:
    >>> valid_exist('John')
    [0, 3, 5]
    """
    # Read the CSV file (make sure the file path is correct)
    df = pandas.read_csv(r'main.csv')

    search_key = search_key.lower()  # Normalize the search term to lowercase

    # Search by name, number, or email, case-insensitive
    name_matches = df[df['Name'].str.lower().str.contains(search_key)]
    if not name_matches.empty:
        return name_matches.index.tolist()
    
    number_matches = df[df['Number'].astype(str).str.contains(search_key)]
    if not number_matches.empty:
        return number_matches.index.tolist()
    
    mail_matches = df[df['Mail'].str.lower().str.contains(search_key)]
    if not mail_matches.empty:
        return mail_matches.index.tolist()
    
    return False  # No match found, return False