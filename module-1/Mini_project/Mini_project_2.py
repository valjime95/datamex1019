import random

# Hangman.

#.....******* Letrero de Hangman*****.........#


alphabet = {
    'A': ((0,0),(0.5,1),(0.75,0.5),(0.25,0.5),(0.75,0.5),(1,0)),
    'B': ((0,0),(0,1),(0.625 ,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5),(0.625,0.5),(0.75,0.375),(0.75,0.125),(0.625,0),(0,0)),
    'C': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'D': ((0,0),(0,1),(0.625 ,1),(0.75,0.875),(0.75,0.125),(0.625,0),(0,0)),
    'E': ((0.75,0),(0,0),(0,0.5),(0.75,0.5),(0,0.5),(0,1),(0.75,1)),
    'F': ((0,0),(0,0.5),(0.75,0.5),(0,0.5),(0,1),(0.75,1)),
    'G': ((0.75,0.5),(0.625,0.5),(0.75,0.5),(0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'H': ((0,0),(0,1),(0,0.5),(0.75,0.5),(0.75,1),(0.75,0)),
    'I': ((0,0),(0.25,0),(0.125,0),(0.125,1),(0,1),(0.25,1)),
    'J': ((0,0.125),(0.125,0),(0.375,0),(0.5,0.125),(0.5,1)),
    'K': ((0,0),(0,1),(0,0.5),(0.75,1),(0,0.5),(0.75,0)),
    'L': ((0,0),(0,1),(0,0),(0.75,0)),
    'M': ((0,0),(0,1),(0.5,0),(1,1),(1,0)),
    'N': ((0,0),(0,1),(0.75,0),(0.75,1)),
    'O': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875),(0.75,0.125)),
    'P': ((0,0),(0,1),(0.625,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5)),
    'Q': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875),(0.75,0.125),(0.875,0)),
    'R': ((0,0),(0,1),(0.625,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5),(0.625,0.5),(0.875,0)),
    'S': ((0,0.125),(0.125,0),(0.625,0),(0.75,0.125),(0.75,0.375),(0.675,0.5),(0.125,0.5),(0,0.625),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'T': ((0,1),(0.5,1),(0.5,0),(0.5,1),(1,1)),
    'U': ((0,1),(0,0.125),(0.125,0),(0.625,0),(0.75,0.125),(0.75,1)),
    'V': ((0,1),(0.375,0),(0.75,1)),
    'W': ((0,1),(0.25,0),(0.5,1),(0.75,0),(1,1)),
    'X': ((0,0),(0.375,0.5),(0,1),(0.375,0.5),(0.75,1),(0.375,0.5),(0.75,0)),
    'Y': ((0,1),(0.375,0.5),(0.375,0),(0.375,0.5),(0.75,1)),
    'Z': ((0,1),(0.75,1),(0,0),(0.75,0)),
}

#Python Turtle
import turtle
import random

myPen = turtle.Turtle()
myPen.hideturtle() #escondemos el cursor
myPen.speed(1) # speed 1 es el más lento
window = turtle.Screen()
window.screensize(1500,1500)
window.bgcolor("#000000")
myPen.pensize(5)

def displayMessage(message,fontSize,color,x,y):
  myPen.color(color)
  message=message.upper()
  
  for i in message:
    if i in alphabet:
      letter=alphabet[i]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen.pendown()
        
      x += fontSize
      
    if i == " ":
      x += fontSize
    x += characterSpacing 

#Programa comienza aquí
fontSize = 43
characterSpacing = 5
fontColor = "#FF00FF"
message = 'Hangman!!'
displayMessage(message,fontSize,fontColor,-300,0)

dibujo = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
nombres = ['Ernesto','Ivan','Diego','Javier','Reynaldo','Ricardo','Jorge','Diego','Fernando','Roger','Santiago','Enrique','Valeria','Juan','Arturo','Raul','Gabriel','Luis']

def buscarPalabraAleat(list):
    name=random.choice(nombres)
    return name
    
def displayBoard(dibujo, letraIncorrecta, letraCorrecta, nombre):
    print(dibujo[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(nombre)
    for i in range(len(nombre)): # Remplaza los espacios en blanco por la letra bien escrita
        if nombre[i] in letraCorrecta:
            espacio = espacio[:i] + nombre[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")

def elijeLetra(let):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in let:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra

def empezar():
    # Esta funcion devuelve talrue si el jugador quiere volver a jugar, de lo contrario devuelve False
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

print ('A H O R C A D O')
letraIncorrecta = ""
letraCorrecta = ""
nombre = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(dibujo, letraIncorrecta, letraCorrecta, nombre)
    # El usuairo elije una letra.
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in nombre:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(nombre)):
            if nombre[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('¡Muy bien! La palabra secreta es "' + nombre + '"! ¡Has ganado!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letraIncorrecta) == len(dibujo) - 1:
            displayBoard(dibujo, letraIncorrecta, letraCorrecta, nombre)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + nombre + '"')
            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            nombre = buscarPalabraAleat(palabras)
        else:
            break