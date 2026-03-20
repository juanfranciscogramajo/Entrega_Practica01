import random

category = {
    "programacion": ["python","programa","variable","funcion","bucle","cadena","entero","lista"],
    "equipos de futbol argentino": ["boca","river","gimnasia","racing","san lorenzo"],
    "marcas de autos": ["ford","chevrolet","toyota","honda","nissan"],
    "paises": ["argentina","brasil","chile","colombia","peru"]
}

puntaje_total = 0

print("¡Bienvenido al Ahorcado!")
print()
print("Categorías disponibles:")
for cat in category:
    print(f"- {cat}")
while True:
    # Solicitar al jugador que elija una categoría válida
    category_Input = input("Elige una categoria: ").lower()
    if category_Input in category:
        category_random= random.sample(category[category_Input], len(category[category_Input])) 
        break
    else:
        print("Categoria no valida, Por favor elige una categoria valida ")
for word in category_random:
    # Cada ronda se reinicia el puntaje de la ronda, las letras adivinadas, y los intentos
    print("===COMIENZA LA RONDA===")
    puntaje_ronda = 0    
    guessed = []
    attempts = 6
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
            puntaje_ronda += 6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
    
        letter_Input = input("Adivina una letra: ").lower() 
        if not letter_Input.isalpha() or len(letter_Input) != 1:
            print("Entrada no valida")
            continue

        if letter_Input in guessed:
            print("Ya usaste esa letra.")
        elif letter_Input in word:
            guessed.append(letter_Input)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter_Input)
            attempts -= 1
            puntaje_ronda -= 1
            print("Esa letra no está en la palabra.")
            print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje_ronda = 0
    print(f"Tu puntaje final de la ronda es: {puntaje_ronda}")
    print ("===FIN DE LA RONDA===")
    puntaje_total += puntaje_ronda
    print( "¿Quieres jugar otra ronda? (s/n)")
    play = input().lower()
    # Si el jugador no quiere jugar otra ronda, se muestra el puntaje final y se termina el juego
    if play != "s": 
        print(f"¡Gracias por jugar! Tu puntaje final es: {puntaje_total}")
        break
else:
    # Esto se ejecuta solo si el 'for' termina de recorrer todas las palabras
    print(f"\n¡Ya no quedan más palabras en esta categoría!")
    print(f"¡Gracias por jugar! Tu puntaje final absoluto es: {puntaje_total}")