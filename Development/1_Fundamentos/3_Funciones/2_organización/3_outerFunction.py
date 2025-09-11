""" Funciones externas - Funciones anidadas
Una función puede estar definida dentro de otra función."""

def outer_function():
    outer_var = "Hello from the outer function!"
    def inner_function():
        print(outer_var)  # Accessible from the enclosing scope
    inner_function()
outer_function()
# Two nested functions, the outer one labeled outer_function and 
# the inner one inner_function