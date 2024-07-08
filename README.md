# Motivational-Quote-Sender
This script sends a motivational quote to a specified email address every Sunday using Gmail's SMTP server.

# Features
Sends a random motivational quote from a file to a specified email address
Only sends emails on Sundays
Uses Gmail's SMTP server for email sending
Supports TLS encryption for secure email transmission

# Getting Started
Clone the repository or download the code.
Create a file called quotes.txt in the same directory as the script and add your motivational quotes, one per line.
Replace my_email and password with your own Gmail credentials.
Replace to_addrs with the email address you want to send the quotes to.
Run the script using Python (e.g., python script.py).

# How it Works
The script checks if the current day is Sunday.
If it is, the script selects a random quote from the quotes.txt file.
The script establishes a connection to Gmail's SMTP server using TLS encryption.
The script logs in to the email account using the provided credentials.
The script sends an email with the subject "Quotes for Motivation" and the selected quote as the body.

# Requirements
Python 3.x
smtplib library (built-in)
datetime library (built-in)
random library (built-in)
Gmail account with SMTP access enabled

# Security Note
Make sure to keep your email credentials secure and do not share them with anyone.
Consider using a secure password storage method, such as environment variables or a secrets manager.
