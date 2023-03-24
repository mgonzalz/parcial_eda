'''
Escriba una clase que permita describir un libro y situar los valores asociados. 
Dar un ejemplo de uso en Python.

'''
class Libro:
    def __init__(self, titulo, autor, editorial, paginas, ano_publicacion, isbn):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.paginas = paginas
        self.ano_publicacion = ano_publicacion
        self.isbn = isbn
    def titulo(self):
        return 'TÍTULO: ' + self.titulo
    def autor(self):
        return 'AUTOR: ' + self.autor
    def editorial(self):
        return 'EDITORIAL: ', self.editorial
    def paginas(self):
        return 'Tiene un total de: ' + str(self.paginas) + ' páginas'
    def ano_publicacion(self):
        return 'Año de publicación: ' + str(self.ano_publicacion)
    def isbn(self):
        return 'ISBN: ' + str(self.isbn)
    def __str__(self): #__str__: Usar para dar información sobre el objeto (descripción informal)
        cadena = self.titulo + ' es un libro escrito por ' + self.autor
        return cadena

libro1 = Libro('El señor de los anillos', 'J.R.R. Tolkien', 'BOOKET', 566, 1954, 9788493801311) #Definimos el objeto libro1
print(libro1.titulo) #Imprimimos el título del libro1
print(libro1.autor) #Imprimimos el autor del libro1
print(libro1) #Devuelve la cadena definida en el método __str__
libro2 = Libro('El corredor del laberinto', 'James Dashner', 'NOCTURNA EDICIONES', 532, 2010, 9788493801311)
print(libro2)
