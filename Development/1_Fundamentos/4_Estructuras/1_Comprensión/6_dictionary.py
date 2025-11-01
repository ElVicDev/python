""" Escribir un programa en Python que cree un diccionario para almacenar 
    información de contacto, incluyendo nombres y números de teléfono. 
    A continuación, realice las siguientes operaciones:
    - Busque el número de teléfono de un contacto específico.
    - Añada un nuevo contacto al diccionario.
    - Actualice el número de teléfono de un contacto existente.
    - Elimine un contacto del diccionario. """

# Create a dictionary to store contact information
contacts = {"Alice": "555-1234", "Bob": "555-5678", "Carol": "555-9012"}

# Look up Bob's phone number
bobs_phone = contacts["Bob"]
print(bobs_phone)
# Output: 555-5678

# Add a new contact
contacts["David"] = "555-4321"

# Update Carol's phone number
contacts["Carol"] = "555-2468"

# Remove Alice's contact information
del contacts["Alice"]

# Print updated contacts
print(contacts)

""" Este ejemplo creó un diccionario llamado contactos para almacenar números 
    de teléfono. 
    Puede recuperar fácilmente el número de Bob utilizando su nombre como clave. 
    A continuación, ha añadido un nuevo contacto ("David") y ha actualizado 
    el número de teléfono de Carol. 
    Por último, has eliminado la entrada de Alicia del diccionario. """