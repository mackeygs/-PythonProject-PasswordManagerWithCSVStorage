# PythonProject-PasswordManagerWithCSVStorage

## Author
Geoffrey Mackey

## Description
A command‑line Password Manager that allows users to securely store, retrieve, update, delete, and generate passwords using a CSV file as a lightweight credential database.

## Features
- Add new credentials (`-add`)
- Retrieve stored credentials (`-get`)
- Update username or password (`-update`)
- Delete an entry (`-delete`)
- Generate and store secure passwords (`-gen`)
- Display help (`-h`)
- Validate site/domain names using regex
- Automatically creates CSV storage if missing
- Handles invalid arguments gracefully

## Requirements
- Python 3.x
- Standard libraries only (csv, argparse, regex, os)


## Usage

### Add Credentials
`python password_manager.py -add example.com user123 MyPass!`

### Retrieve Credentials
`python password_manager.py -update example.com password NewSecurePass!`

### Delete Entry
`python password_manager.py -delete example.com`

### Generate a Secure Password
`python password_manager.py -gen example.com user123 16`

### Display Help
`python password_manager.py -h`

### How It Works
- Stores all credentials in a passwords.csv file.
- Validates site names (e.g., example.com) using a regular expression.
- Auto‑creates the CSV with headers if it doesn't exist.
- Uses Python's argparse to parse flags and handle incorrect usage.
- Secure password generator uses letters, digits, and symbols.

### Examples
- python password_manager.py -add example.com admin P@ss123
- python password_manager.py -get example.com
- python password_manager.py -update example.com password NewPass!
- python password_manager.py -gen test.com user123 16
- python password_manager.py -delete example.com

### License
Open source, free to use.
