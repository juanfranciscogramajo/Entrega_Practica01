import random
from turtle import left
category = {
    "programacion": ["python","programa","variable","funcion","bucle","cadena","entero","lista"],
    "equipos de futbol argentino": ["boca","river","gimnasia","racing","san lorenzo"],
    "marcas de autos": ["ford","chevrolet","toyota","honda","nissan"],
    "paises": ["argentina","brasil","chile","colombia","peru"]
}
word = random.choice(category)
guessed = []
attempts = 6
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()
print("Categorías disponibles:")
for cat in category.keys():
    print(f"- {cat}")
while True:
    categoryInput = input("Elige una categoria: ").lower()
    if categoryInput in category:
        word = random.choice(category[categoryInput])
        break
    else:
        print("Categoria no valida, Por favor elige una categoria valida ")
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntaje += 6
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letterInput = input("Adivina una letra: ")
    if letterInput.isalpha() and len(letterInput) > 1:
        print("Entrada no valida")
        continue
    letter = letterInput 

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje = 0
print(f"Tu puntaje final es: {puntaje}") 
