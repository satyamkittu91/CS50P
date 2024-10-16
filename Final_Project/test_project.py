import pytest
import csv
from contact_manager import add_contact, update_contact, remove_contact, search_contact, search_info_contact, search_print_contact
from test_data import generate_random_contact
from validation import valid_name, valid_number, valid_mail, valid_category, valid_country, valid_exist
import validation
import contact


# Validation tests
def test_valid_name():
    assert valid_name("John Doe") == "John Doe"
    assert valid_name("Doe, John") == "John Doe"
    assert not valid_name("123")
    assert not valid_name("")

def test_valid_number():
    assert valid_number("+1234567890") == "+1234567890"
    assert valid_number("123-456-7890") == "1234567890"
    assert not valid_number("abc")
    assert not valid_number("")

def test_valid_mail():
    assert valid_mail("john.doe@example.com") == "john.doe@example.com"
    assert not valid_mail("invalid_email")
    assert not valid_mail("")

def test_valid_category():
    assert valid_category("Friends") == "Friends"
    assert not valid_category("Invalid Category")

def test_valid_country():
    assert valid_country("United States") == "United States"
    assert not valid_country("Invalid Country")

def test_valid_exist():
    contact_data = generate_random_contact()
    add_contact(**contact_data)

    # Search for the contact by name
    result = valid_exist(contact_data['Name'])
    assert result

    # Search for a non-existent contact
    result = valid_exist("Non-existent Contact")
    assert not result


# Contact manager tests
def test_add_contact():
    contact_data = generate_random_contact()
    add_contact(**contact_data)

    # Verify that the contact was added to the CSV file
    with open('main.csv', 'r') as f:
        reader = csv.DictReader(f)
        found = False
        for row in reader:
            if row['Name'] == contact_data['Name'] and \
               row['Number'] == contact_data['Number'] and \
               row['Mail'] == contact_data['Mail']:
                found = True
                break
    assert found

def test_update_contact():
    contact_data = generate_random_contact()
    add_contact(**contact_data)

    # Update the contact's name
    new_name = "Updated Name"
    index_point = search_contact(validation.valid_exist(contact_data['Name']))
    update_contact(index_point, 'Name', new_name)

    # Verify that the name was updated in the CSV file
    with open('main.csv', 'r') as f:
        reader = csv.DictReader(f)
        found = False
        for row in reader:
            if row['Name'] == new_name and \
               row['Number'] == contact_data['Number'] and \
               row['Mail'] == contact_data['Mail']:
                found = True
                break
    assert found

def test_remove_contact():
    contact_data = generate_random_contact()
    add_contact(**contact_data)

    # Remove the contact
    remove_contact(search_contact(validation.valid_exist(contact_data['Name'])))

    # Verify that the contact was removed from the CSV file
    with open('main.csv', 'r') as f:
        reader = csv.DictReader(f)
        found = False
        for row in reader:
            if row['Name'] == contact_data['Name'] and \
               row['Number'] == contact_data['Number'] and \
               row['Mail'] == contact_data['Mail']:
                found = True
                break
    assert not found

def test_search_contact():
    contact_data = generate_random_contact()
    add_contact(**contact_data)

    # Search for the contact by name
    result = search_contact(validation.valid_exist(contact_data['Name']))
    assert search_print_contact(result).to_dict()['Name'] == contact_data['Name']

def test_search_info_contact():
    contact_data = generate_random_contact()
    add_contact(**contact_data)

    # Search for the contact's name
    result = search_info_contact(search_contact(validation.valid_exist(contact_data['Name'])), 'Name')
    assert result == f"Name: {contact_data['Name']}"
