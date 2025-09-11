""" Ejemplo de uso de una Variable Global """

# Global variable
COMPANY_NAME = "Global Tech Solutions"

def print_welcome_message():
    print("Welcome to", COMPANY_NAME.upper())

def print_contact_info():
    print("Contact", COMPANY_NAME, "at info@globaltechsolutions.com") 

# Output: Welcome to GLOBAL TECH SOLUTIONS
print_welcome_message()

# Output: Contact Global Tech Solutions at info@globaltechsolutions.com
print_contact_info()