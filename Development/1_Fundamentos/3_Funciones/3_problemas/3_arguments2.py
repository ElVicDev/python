# Parámetros obligatorios y opcionales

def create_user_profile(name, age, occupation="Student", interests=None): # Use None as default
    """
    Creates a user profile with optional interests.

    Args:
        name (str): The user's name (required).
        age (int): The user's age (required).
        occupation (str, optional): The user's occupation (defaults to "Student").
        interests (list, optional): A list of the user's interests (defaults to None).
    """
    if interests is None:  # Initialize if None
        interests = [] 

    profile = {
        "name": name,
        "age": age,
        "occupation": occupation,
        "interests": interests
    }

    return profile

# Usage
user1 = create_user_profile("Alice", 25, "Software Engineer", ["Coding", "Hiking"])
user2 = create_user_profile("Bob", 18)  # Uses default occupation and no interests
user3 = create_user_profile("Carol", 30, interests=["Gardening", "Reading"])

print(user1)
print(user2)
print(user3)

# Explicación
""" Definición de la función: 
        La función create_user_profile encapsula la tarea de crear un 
        perfil de usuario. Esto promueve la modularidad, haciendo nuestro código 
        más organizado y reutilizable.
    Parámetros obligatorios y opcionales:
        name y age son parámetros obligatorios porque un perfil de usuario 
        no estaría completo sin ellos.
        occupation y interests son opcionales. 
        occupation es por defecto "Estudiante", un escenario común para muchos usuarios. 
        interests es por defecto None, lo que permite a los usuarios omitir esta 
        información si así lo desean.
    Documentación clara: 
        La docstring al principio de la función explica su propósito, 
        los argumentos esperados y sus tipos. 
        Esta documentación es muy valiosa tanto para usted como para otros 
        desarrolladores que puedan utilizar su función.
    Valores por defecto: 
        El valor por defecto de occupation garantiza que la función pueda 
        crear un perfil básico aunque no se proporcionen esos detalles.
    Manejo de intereses opcionales: 
        interests se establece en None por defecto. 
        Dentro de la función, se comprueba si interests es None y, en caso 
        afirmativo, se inicializa con una lista vacía. 
        Esto garantiza que cada llamada a la función obtenga una lista de 
        intereses nueva y vacía, evitando así efectos secundarios no deseados.
    Argumentos de palabra clave: 
        En el tercer ejemplo de uso (user3), utilizamos explícitamente un 
        argumento de palabra clave (interests) para aclarar para qué parámetro 
        opcional estamos proporcionando un valor. 
        Esto mejora la legibilidad del código. """