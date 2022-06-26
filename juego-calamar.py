mport random
intentosRealizados = 0
numero = random.randint(1, 100)
print("Juego del Calamar. Adivina el número secreto o morirás.")
print("Quiero saber quién eres. Escribe tu nombre.")
nombre = input()
print("Jugador", nombre, "," " tienes diez intentos para salvar tu vida. ¿Quieres continuar? Responde si o no.")
resp = input ()
while (resp == "si","no"):
  if (resp == "si"):
   print("Muy bien. Eres valiente. Escribe tu primer intento")
  if (resp == "no"):
    print("Te jodiste. Igual debes continuar o morirás. Escribe tu primer intento.")
  break
while intentosRealizados < 10:
 estimacion = input()
 estimacion = int(estimacion) 
 intentosRealizados = intentosRealizados + 1
 if estimacion < numero:
  print("Tu estimación es muy baja. Te quedan", 10-intentosRealizados, "intentos")
 if estimacion > numero:
  print('Tu estimación es muy alta. Te quedan', 10-intentosRealizados,"intentos")
 if estimacion == numero:
  break;
if estimacion == numero:
 print('¡Has adivinado el número secreto en ' , intentosRealizados , 'intentos! Te salvaste')
if estimacion != numero:
 print('El número era', numero,"; Vas a morir.")
