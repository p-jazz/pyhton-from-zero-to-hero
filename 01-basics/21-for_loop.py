# Python los string ya son varios valores en uno. Cada string está compuesto de caracteres o letras.
some_text = "Algun texto de ejemplo"
# En un texto podemos acceder a cada letra utilizando los [] e indicando su posición partiendo desde 0
print(some_text[0])
print(some_text[1])
print(some_text[2])

# En python los string son colecciones de caracteres. Veremos otras colecciones mas adelante, como las listas y los diccionarios
# Las colecciones las podemos recorrer con el loop for que va a ejecutar su cuerpo una vez por cada elemento de la colección

for letter in some_text:
    print(letter)

for num in reversed(range(11)):
    print(num)
print("BOMB")