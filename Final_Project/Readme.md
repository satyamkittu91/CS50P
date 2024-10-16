
# Contact Manager Project

## What’s This All About?

Welcome to **Contact Manager**, your new best friend for keeping track of all your contacts, whether they're friends, coworkers, or even that long-lost cousin. This project was built as the final project for Harvard’s CS50P course, combining all the cool stuff I learned along the way—like file handling, data validation, and user-friendly interfaces. 

The Contact Manager makes it easy to manage your contacts with just a few simple commands. Want to add someone new? No problem. Need to update their details? Piece of cake. Can't remember a phone number? We’ve got search for that. All of it’s done via an intuitive command-line interface that’s designed to be as painless (and even a bit fun!) as possible.

## What’s in the Box?

This project is split into a few different files, each doing its own special job:

### 1. **`contact.py`**:
This is where each contact comes to life! It holds the `Contact` class, which represents all the details of a contact, like their name, number, email, category (are they a friend or a colleague?), and their country. The `Contact` class also knows how to transform its details into a dictionary so we can store it easily.

### 2. **`validation.py`**:
This is the bouncer of the project, making sure all the input data is valid. It checks if the name, number, email, category, and country you’re adding make sense. If something's off (like a missing name or an invalid email), it stops you before you mess up your contact list. It’s all about keeping your data clean and safe!

### 3. **`contact_manager.py`**:
This is the brain behind all the contact management. Whether you're adding, updating, deleting, or searching for a contact, this file has the logic to make it happen. It reads and writes to the contact list (stored in a CSV file) and makes sure your contacts are always up-to-date.

### 4. **`user_interface.py`**:
This is the voice of the whole project—the command-line interface where you’ll interact with the program. It guides you through commands like adding new contacts, searching for people, or updating their info. This is also where we provide help and explanations if you ever feel lost (just type "help" or "commands").

### 5. **`project.py`**:
This is the main execution file which is called in the terminal. And which triggers the whole Project.

### 6. **`main.csv`**:
This is where all your contacts live. Don’t worry if it’s not there the first time you run the program—it’ll be created automatically the moment you add your first contact. Your data is stored in a simple, easy-to-read format (CSV), so you can always check it or edit it directly if you like.

## Design Choices: Why I Did What I Did

### Breaking Things Into Pieces
One of the first choices I made was to break the code into smaller, focused files. Each file has its own job, making it easier to maintain and understand. The modular design also makes it super simple to add new features or fix bugs without breaking everything else.

### Keeping It Simple With CSV
I decided to store contact data in a CSV file because it’s lightweight, easy to manage, and doesn’t need a full database setup. Plus, the pandas library makes it really easy to work with this format, even if your contact list grows large. So, while this project is simple, it’s also scalable.

### Focus on Validation
Good data is key, right? That’s why I spent a lot of time making sure the validation works properly. It checks for things like whether a name starts with a letter, if the phone number looks right, and if the email address makes sense. This way, we avoid any “oops” moments where you accidentally add bad data to your list.

### User Experience Matters
The command-line interface is straightforward and easy to use. I made sure that the prompts are clear and that the error messages help you understand exactly what went wrong. Plus, if you’re about to make a big change (like deleting a contact), the program double-checks with you—just to make sure!

## Final Thoughts

This Contact Manager project was a great way to bring everything I’ve learned from CS50P into one cohesive app. From managing data to creating an intuitive user experience, I tried to design something that’s not just functional but also enjoyable to use. I hope you find it as helpful as I’ve enjoyed building it!

Happy contact-managing!
