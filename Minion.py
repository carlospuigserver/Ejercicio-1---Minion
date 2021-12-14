# Declaro las variables
palabra=input("Escribe una palabra  ")
Vocales=['AEIOU']
l=len(palabra) #longitud de la palabra
consonantes=0
vocales=0

for i in range(l):
    if palabra[i] in Vocales:
        vocales+=l-i
        
    else:
        consonantes+=l-i
        


print("Kevin",vocales)
print("Stuart",consonantes)





if consonantes<vocales:
    print("El ganador es Kevin con ",vocales,"puntos")
if consonantes>vocales:
    print("El ganador es Stuart con ",consonantes,"puntos")
if consonantes==vocales:
    ("La partida ha sido empatada a",consonantes,"puntos")
print(" El número total de puntos obtenidos entre Kevin y Stuart es de ",consonantes+vocales,"puntos")