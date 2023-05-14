# Personal data

## what is user-data

User data is any information that can be used to identify a person. It can be anything from a name, email address, photo, bank details, posts on social networking websites, medical information, or a computer IP address.

## Topic Covered

- What PII stands for
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

## Tasks

### [0. Regex-ing](./0-regex-ing)

Write a function called filter_datum that returns the log message obfuscated:

- Arguments: a line from a log file containing a date, an IP, a request route, a user ID and a message (in this order)
- The function should use a regex to replace occurrences of certain field values
- filter_datum should return the log message **obfuscated**
- The function should use the following patterns:
  - `a date` (from January 1st, 2021 to December 31th, 2021) - replace it with `**/redacted_date**`
  - `an IP`
    - replace it with `**/redacted_ip**`
    - An IP is an IPv4 address with the pattern `X.X.X.X` where `X` is a digit
    - `a password` (any password equal or longer than 8 characters) - replace it with `**/redacted_pwd**`
    - `a user ID` (a positive integer) - replace it with `**/redacted_user_id**`
    - Returns the log message **obfuscated**
    - Format: `YYYY-mm-dd hh:mm:ss x.x.x.x yyyyyyyy zzzzzzzzzzzzzzzz`

### [1. Log formatter](./1-log_formatter.py)

updating the class to accept a list of strings representing fields to obfuscate
### [2. Create logger](./2-create_logger.py)

Create logger

### [3. Connect to secure database](./3-connect_db.py)

connect to secure database

### [4. Read and filter data](./filtered_logger.py)

Read and filter data

### [5. Encrypting passwords](./encrypt_password.py)

Encrypting passwords

### [6. Check valid password](./auth.py)

Check valid password

## Technologies Used

- Python 3.9
- Git
- MySQL