

class Contact():
    """
    Represents a contact in the PeoplePal system with full contact details.
    
    This class encapsulates all contact information with proper validation
    and formatting. It includes properties for safe access to private fields
    and methods for string representation and dictionary conversion.
    
    Attributes:
        name (str): Contact's full name
        _number (str): Phone number (private)
        _mail (str): Email address (private)
        category (str): Contact category (e.g., Work, Family)
        last_update (date): Last modification date
        country (str): Country name with code
        
    Properties:
        number: Getter/setter for phone number
        mail: Getter/setter for email
        
    Methods:
        __str__: Returns formatted contact information
        to_dict: Converts contact to dictionary format
        
    Example:
        >>> contact = Contact("John Doe", "+1234567890", 
                            "john@example.com", "USA", 
                            "2024-01-01", "Work")
        >>> print(contact)
        Contact Information
        Name: John Doe
        Number: +1234567890
        ...
    """


    def __init__(self, name, number, mail, country, last_update, category='Uncategorized'):
        """
        Initialises a Contact object

        : name: The name of the contact
        : number: The phone number of the contact
        : mail: The email address of the contact
        : country: The country of the contact
        : last_update: The date of the last update of the contact
        : category: The category of the contact (default is 'Uncategorized')
        """
        self.name = name
        self._number = number
        self._mail = mail
        self.category = category
        self.last_update = last_update
        self.country = country

        
    @property
    def number(self):
        
        return self._number

    @number.setter
    def number(self, value):
        
        self._number = value

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, value):
        self._mail = value



    def __str__(self):
        return (f"Contact Information\n"
                f"Name : {self.name}\n"
                f"Number : {self._number}\n"
                f"Mail : {self._mail}\n"
                f"Category : {self.category}\n"
                f"Country : {self.country}\n"
                f"Last Updated : {self.last_update}")
    
    def to_dict(self):
        """
        Return a dictionary representation of the contact's information
        
        :return: A dictionary with the contact's information
        """
        contact_dict = {
            'Name' : self.name,
            'Number': self._number,
            'Mail': self._mail,
            'Category': self.category,
            'Country': self.country,
            'Last Update': self.last_update
        }
        return contact_dict
    
    

