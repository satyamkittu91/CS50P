# PeoplePal
#### Video Demo: https://youtu.be/86_tua3eVu8?si=sII-IQMFVM9juknh

## What's This All About?

Welcome to **PeoplePal**, your ultimate tool for keeping track of everyone in your life—friends, family, colleagues, or anyone you want to stay connected with. This project is the culmination of everything I’ve learned in Harvard’s CS50P course, blending skills like file handling, data validation, modular programming, and designing user-friendly tools.

With Contact Manager, managing your contacts is effortless. Whether you’re adding, searching, updating, or organizing, it’s all handled through an intuitive command-line interface that’s simple, clear, and easy to use.

## What’s in the Box?

This project is made up of a few files, each with a specific role to play:

### 1. **`contact.py`**
This file contains the `Contact` class, which represents the details of each contact—like name, phone number, email, category, and country. The class also makes it easy to convert these details into a dictionary for storing.

### 2. **`validation.py`**
This module ensures that all the inputs you provide are valid. From checking that names and numbers make sense to verifying email addresses, it acts as a safeguard to keep your contact list clean and error-free.

### 3. **`contact_manager.py`**
The brain of the project, this file handles all the operations—adding, updating, deleting, and searching for contacts. It ensures your contact list (stored in a CSV file) is always up-to-date.

### 4. **`settings.py`**
This module allows you to create and manage contact categories. You can even set a default category to streamline adding new contacts, making organization simple and personalized.

### 5. **`user_interface.py`**
This is where the magic happens—your command-line interface for interacting with the Contact Manager. From here, you can navigate the program, execute commands, and get help if needed. The main file that brings everything together. Run this file to start managing your contacts right away.

### 6. **`categories.txt`**
This file keeps track of all your contact categories, including custom ones. It updates automatically whenever you make changes.

### 7. **`main.csv`**
This is your contact database, where all your contacts are stored. If it doesn’t exist yet, the program will create it automatically when you add your first contact. It’s stored in CSV format, so you can also view or edit it manually if needed.

## Design Choices: Why I Did What I Did

### **Modular Design**
Each file in the project serves a distinct purpose, keeping the code clean and manageable. This structure makes it easier to add new features or make improvements without disrupting existing functionality.

### **Data Validation**
To ensure the integrity of your data, I implemented a thorough validation system. It checks for common errors and prevents invalid entries, keeping your contact list accurate and reliable.

### **Contact Organization**
Categories make it easy to group and organize your contacts. Whether you’re dividing them by personal and professional or creating custom groups, it’s all flexible and user-friendly.

### **User Experience**
The command-line interface is designed to be straightforward, with clear prompts and helpful messages guiding you every step of the way. Safety checks, such as confirmations for deletion, make the experience reliable and stress-free.

### **Lightweight and Accessible**
Using CSV and JSON for data storage keeps the project lightweight and easy to set up—no need for complex database systems. Plus, it’s scalable for larger contact lists.

## How to Use

1. Download or clone the project files.
2. Open your terminal and run `project.py` to start the program.
3. Follow the on-screen instructions to add, search, update, or organize your contacts.
4. Use the `commands` command to see available actions or type `help <command>` for detailed guidance.

## Final Thoughts

The **PeoplePal** project is a practical application of everything I’ve learned, designed to be functional, simple, and enjoyable to use. I hope it serves as a handy tool for organizing your connections, and I’m excited to see it in action. Happy contact-managing! 😊