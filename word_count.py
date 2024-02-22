import sys

txt = sys.argv[1]
with open(txt, "r") as  file:
    texto = file.read()
set_txt = [len(set(texto)), len(set(texto.split(" ")))]

print(f"El número de caracteres distintos es: {set_txt[0]} \nEl número de palabras distintas es: {set_txt[1]}") 
