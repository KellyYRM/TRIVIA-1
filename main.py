BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import time
puntaje = 0
iniciar_trivia = True 
intentos = 0 
print(YELLOW+'¡Bienvenido a la trivia sobre nuestro país, PERÚ!.\n'+RESET)
time.sleep(2)
print(BLUE+"INDICACIONES"+RESET)
time.sleep(1)
print("1). Tienes", puntaje, "puntos, veremos cuanto sumas.")
import random  # Importamos la librería random
puntaje = random.randint(0, 10)
print("Cada pregunta correcta vale 10 puntos y cada pregunta incorrecta resta 5 puntos.\n")
time.sleep(2)
print("2). Para hacer más divertido está trivia haremos que tengas un puntaje random\n")
time.sleep(2)
print("3). La última pregunta puede sumar o multiplicar tu puntaje si tu respuesta es correcta o algo acertada, pero  si tu respuestas es incorrecta o totalmente absurda puede restar o dividir tu puntaje. ¡SUERTE!\n")
time.sleep(2)
print(MAGENTA+'Con solo tres preguntas pondremos a prueba tu identidad como peruano\n'+RESET)
time.sleep(2)
nombre = input(BLUE+"Ingresa tu nombre: "+RESET)
print('\nHola', nombre,'responde las siguentes preguntas escribiendo la letra de la alternativa y presiona "Enter" para enviar la respuesta:\n')
time.sleep(2)
print(RED+"\nOJO",nombre,"asegurate que tu respuesta este en minuscula.\n"+RESET)
time.sleep(2)
print(YELLOW+"EMPECEMOS\n"+RESET)
time.sleep(2)
while iniciar_trivia == True:
  intentos += 1
  puntaje = 0
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
 #pregunta 1
  print("1) ¿Cuál es la montaña más alta en el Perú?\n")
  print("   a) Huandoy")
  print("   b) Coropuna")
  print("   c) Huantsan")
  print("   d) Huascarán")
  respuesta_1 = input("\nTu respuesta:") 
  if respuesta_1 == "d": 
    puntaje += 10 
    print(YELLOW+"\nMuy bien", nombre, "veamos que tal te va con la siguinte...\n"+RESET)
  elif respuesta_1 == "x": 
    puntaje += 100
    print(RED+"este es un mensaje secreto\n"+RESET)
  else: 
   puntaje -= 5 
   print(CYAN+"No, ese no era", nombre,"la siguiente seguro te la sabes...\n"+RESET)
  while respuesta_1 not in ("a", "b", "c", "d", "x"):
   respuesta_1 = input("Debes responder a, b, c o Ingresa nuevamente tu respuesta:\n")
   print(nombre, MAGENTA+"llevas", puntaje, 
  "puntos\n"+RESET)
  time.sleep(5)
  #pregunta 2
  print("2) ¿Quién fue el último soberano inca?\n")
  print("   a) Atahualpa")
  print("   b) Huayna Cápac")
  print("   c) Huiracocha")
  print("   d) Manco Capac")
  respuesta_1 = input("\nTu respuesta:")
  if respuesta_1 == "a": 
   puntaje += 10
   print(YELLOW+"¡Correcto!", nombre,"me sorprendes\n"+RESET)
  elif respuesta_1 == "b":
   puntaje -= 5  
   print(CYAN+"¡Incorrecto!", nombre, "Huayna Capac fue el undécimo inca.\n"+RESET)
  elif respuesta_1 == "c": 
   puntaje -= 5 
   print(CYAN+"¡Incorrecto!", nombre, "Huiracocha, fue el octavo gobernante del Curacazgo del Cuzco.\n"+RESET)
  elif respuesta_1 == "d":
   puntaje -= 5 
   print(CYAN+"¡incorrecto!", nombre, "Manco Capac fue el primer emperador incaico.\n"+RESET)
  while respuesta_1 not in ("a", "b", "c", "d", "x"):
   respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:\n")
  if respuesta_1 == "x": 
   puntaje += 100
   print(RED+"este es un mensaje secreto\n"+RESET)
   print(nombre, MAGENTA+"llevas", puntaje, "puntos\n"+RESET)
  time.sleep(5)
 #pregunta 3
  print("3) ¿Quién es conocido  como EL NEWTON PERUANO?\n")
  print("   a) Federico Sal y Rosas")
  print("   b) Federico Villareal")
  print("   c) Santiago Antúnez De Mayolo")
  print("   d) Pedro Paulet")
  respuesta_1 = input("\nTu respuesta:")
  if respuesta_1 == "a":
   print (CYAN+"¡Totalmente incorrecto! ..."+RESET)
   puntaje = puntaje / 2
  elif respuesta_1 == "b":
   print(YELLOW+"Fascinante ", nombre, "es... ¡CORRECTO!\n"+RESET)
   puntaje = puntaje * 2
  elif respuesta_1 == "c":
   print (CYAN+"¡Incorrecto! ..."+RESET)
   puntaje = puntaje - 5
  elif respuesta_1 == "d":
   puntaje = puntaje + 5
   print(CYAN+"No, ese no era", nombre,"pero no importa.\n"+RESET)
  elif respuesta_1 == "x": 
   puntaje += 100
   print(RED+"este es un mensaje secreto\n"+RESET)
  while respuesta_1 not in ("a", "b", "c", "d", "x"):
   respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:\n")
  time.sleep(3)
  print(GREEN+"Felicitaciones llegaste al final, eres un gran PERUANO.\n"+RESET)
  print (MAGENTA+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":
   print("\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False 