""" Crea un conjunto de lenguajes de programación. """

# Create a set of favorite programming languages
languages = {"Python", "JavaScript", "Java"}

# Add "C++" to the set
languages.add("C++")

# Try to add "Python" again (it won't be added because it's a duplicate)
languages.add("Python")
print(languages)  # Output: {'Python', 'C++', 'JavaScript', 'Java'} (order may vary)

# Remove "Java"
languages.remove("Java")

# Create another set of languages
web_languages = {"JavaScript", "HTML", "CSS"}

# Find common languages between the two sets
common_languages = languages.intersection(web_languages)
print(common_languages)  # Output: {'JavaScript'}

""" Observa que añadir "Python" dos veces no tiene ningún efecto 
    debido a la propiedad de unicidad del conjunto. 
    A continuación, se realizaron operaciones con conjuntos para 
    encontrar elementos comunes entre dos conjuntos. """