# Declaro las variables
palabra=input()
Vocales=['AEIOU']
l=len(palabra) #longitud de la palabra
consonantes=0
vocales=0








if consonantes<vocales:
    print("El ganador es Kevin con ",vocales,"puntos")
if consonantes>vocales:
    print("El ganador es Stuart con ",consonantes,"puntos")
if consonantes==vocales:
    ("La partida ha sido empatada a",consonantes,"puntos")
print(" El número total de puntos obtenidos entre Kevin y Stuart es de ",consonantes+vocales,"puntos")