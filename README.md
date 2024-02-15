# inet_4031_adduser_script

Automated User Creation Script for Linux
Description
This Python script automates the process of creating user accounts on Linux systems. Designed as a part of the INET 4031 course, it simplifies user management by reading from an input file (create-users.input) and executing user creation commands based on the provided details.

Features
Automated Creation: Batch process user account creation to save time and reduce manual errors.
Group Assignment: Automatically assigns each new user to specified groups.
Custom User Details: Supports custom names, home directories, and shell types as specified in the input file.
Prerequisites
Linux Operating System with Python 3.x installed.
Sudo privileges for the executing user.
Installation
Clone this repository to your local machine:

bash

git clone https://github.com/DinNguyen88/inet_4031_adduser_script.git
cd inet_4031_adduser_script
Make the script executable:

bash

chmod +x create-users.py
Usage
Prepare your create-users.input file in the following format:

ruby

username:password:FirstName:LastName:Group
Execute the script with:

bash

sudo ./create-users.py < create-users.input
or

bash

cat create-users.input | sudo ./create-users.py
How It Works
The script parses each line of the input file, extracting user information and using system commands to create accounts and set initial passwords. It checks for the presence of a '#' at the start of a line to ignore comments.


Acknowledgments
Joe Axberg (jaxberg@umn.edu) for providing the project outline.
