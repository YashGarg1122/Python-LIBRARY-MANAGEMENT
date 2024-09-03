# Python Library Management System with MySQL

# Project Overview

This Python project is a simple Library Management System that uses MySQL as the backend database. The project allows users to manage library operations such as issuing and returning books and provides an admin panel to view, edit, or delete records. This system is designed for small to medium-sized libraries and is built as a college project for SRM University Delhi-NCR.

# Features

- *Admin Panel*: 
  - View all books issued.
  - Edit issued book data.
  - Delete records.
  
- *Student Portal*:
  - Issue new books.
  - Return books.
  - View all issued books.

- *Database Management*:
  - Automatic database creation and connection.
  - Simple error handling for database connection and management.

# Installation

## Prerequisites
- Python 3
- MySQL Server
- MySQL Connector for Python (`mysql-connector-python`)

## Setting Up the Project

1. *Install MySQL Connector*:
   ```
   pip install mysql-connector-python
   ```

2. *Run the Script*:
   ```
   python main.py
   ```

   The script will prompt for the MySQL root password. Ensure your MySQL server is running locally with the default settings (host: `localhost`, user: `root`).

4. *Database Setup*:
   - The script will automatically check for an existing database named `pyplm`.
   - If the database does not exist, it will create a new one and set up the required tables.

## Usage

1. *Admin Login*: Use the default password `admin` to access the admin panel.
2. *Student Portal*: Students can issue or return books by entering their student ID and the book's UPC code.

## Error Handling

- If the MySQL server is not installed, the script will display an error message.
- The script provides up to three attempts to input the correct MySQL root password.
- If the connection fails after three attempts, the script offers an option to manually input the MySQL connection details.

## Credit

- *Project Version*: 1.0 BETA
- *Developed By*: Yash Garg
- *Team Members*: Dhruv Gupta, Apurva Bansal, Ritesh Kumar Sinha
- *Contact*: [connect.yashgarg@gmail.com](mailto:connect.yashgarg@gmail.com)
- *Institution*: SRM University Delhi-NCR, 3rd SEM, B.Tech (CSE)

This is an open-source project built for educational purposes. Feedback and contributions are welcome!

## License

This project is licensed under the GPL V3 License.

---

Enjoy managing your library with ease!
