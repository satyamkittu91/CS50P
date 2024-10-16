import faker

def generate_random_contact():
    fake = faker.Faker()
    contact_data = {
        'Name': fake.name(),
        'Number': fake.phone_number(),
        'Mail': fake.email(),
        'Category': fake.random_element(['Friends', 'Work', 'Family', 'Acquaintances', 'Other']),
        'Country': fake.country()
    }
    return contact_data