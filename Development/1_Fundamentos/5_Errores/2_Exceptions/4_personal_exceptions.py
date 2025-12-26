# Crear excepciones personalizadas
""" Las excepciones incorporadas en Python cubren una amplia gama de escenarios, 
    pero a veces te encontrarás con errores que no encajan perfectamente en 
    ninguno de ellos. En estos casos, puedes crear excepciones personalizadas: """

class InvalidCredentialsError(Exception):
    pass

# ... later in your code ...
if not valid_credentials(username, password):
    raise InvalidCredentialsError("Incorrect username or password")

""" Las excepciones personalizadas le permiten describir con precisión las 
    condiciones de error específicas de su aplicación, lo que da lugar a mensajes 
    de error más informativos y a un código más claro. 
    Por ejemplo, en una aplicación web, podrías definir excepciones personalizadas 
    para fallos de autenticación, errores de autorización o situaciones de recurso 
    no encontrado. """