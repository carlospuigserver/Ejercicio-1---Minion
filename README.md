Examen

Ejercicio 2 : Ajedrez Torres

La dirección GitHub de este repositorio es: https://github.com/carlospuigserver/Examen.git

Para realizar este código, hemos usado una estructura muy parecida a la del código de la tarea del ajedrez del campus, ha sido muy importante tener muy controlados los casos en los que las piezas tanto blancas como negras quedan encerradas por las fichas rivales y estas no se pueden mover, por tanto se define el ganador, todo esto a partir de las funciones creadas y con, if, else, elif.
Para este código han sido usadas muchas funciones, para crear el tablero,tener una forma de desplazamiento....


El código que he usado para realizar este programa es el siguiente:
```
from random import randint
def inmovil(f,c):
    if f==0 and tablero[f+1][c]!='':
        fallo=True
    elif f==1:
        if tablero[f+1][c]!='' and tablero[f-1][c]!='':
            fallo=True
        else:
            fallo=False
       
    elif f==2 and tablero[f-1][c]!='':
        fallo=True
    else:
            fallo=False
    return fallo   

def impr_tablero(tablero):
    cont_indice=0
    for tablero[cont_indice] in tablero:
        print(tablero[cont_indice])
        cont_indice+=1
        print("\n")

def desplazamiento(f,c):
    if f ==0:
        tablero[f+1][c]=tablero[f][c]
        tablero[f][c]=''
    elif f ==1:
        if tablero[f+1][c] !='':
            tablero[f-1][c]=tablero[f][c]
            tablero[f][c]=''
        else:
            tablero[f+1][c]=tablero[f][c]
            tablero[f][c]=''
    elif f ==2:
        tablero[f-1][c]=tablero[f][c]
        tablero[f][c]=''

           
def alteración(f, c):
    if f == 0:
        f = f + 1
    elif f == 1:
        if tablero[f+1][c] != ' ':
            f= f - 1
        else:
            f = f + 1
    elif f == 2:
        f= f- 1
    return f
    
while True:
    tablero =  [
    [' ', ' ', ' '], 
    [' ', ' ', ' '],
    [' ', ' ', ' '], 
    ]

    x = randint(0,2)
    y = randint(0,2)
    z = randint(0,2)
    a = randint(0,2)
    b = randint(0,2)
    c = randint(0,2)

    while x == a:
        a = randint(0,2)
    while y == b:
        b = randint(0,2)
    while z == c:
        c = randint(0,2)

    
    (tablero[x])[0] = chr(0x2656)
    (tablero[y])[1] = chr(0x2656)
    (tablero[z])[2] = chr(0x2656)
    (tablero[a])[0] = chr(0x265C)
    (tablero[b])[1] = chr(0x265C)
    (tablero[c])[2] = chr(0x265C)

    impr_tablero(tablero)

    errorx = encerrada(x, 0)
    errory = encerrada(y, 1)
    errorz = encerrada(z, 2)
    errora = encerrada(a, 0)
    errorb = encerrada(b, 1)
    errorc = encerrada(c, 2)

    if errorx == True and errory == True and errorz == True:
        print("El jugador blanco no se puede mover, volvemos a crear el tablero")
        pass
    elif errora == True and errorb == True and errorc == True:
        print("El jugador negro no se puede mover, volvemos a crear el tablero")
        pass
    else:
        break

turno = randint(0, 1)
while True:
    if turno == 1:
        if errorx == False and errora == False:
            desplazamiento(x, 0)
            x = alteración(x, 0)
            errora = inmovil(a, 0)
        elif errory == False and errorb == False:
            desplazamiento(y, 1)
            y = alteración(y, 1)
            errorb = encerrada(b, 1)
        elif errorz == False and errorc == False:
            desplazamiento(z, 2)
            z = alteración(z, 2)
            errorc = encerrada(c, 2)
        elif errorx == False:
            desplazamiento(x, 0)
            x = alteración(x, 0)
            errora = encerrada(a, 0)
        elif errory == False:
            desplazamiento(y, 1)
            y = alteración(y, 1)
            errorb = encerrada(b, 1)
        elif errorz == False:
            desplazamiento(z, 2)
            z = alteración(z, 2)
            errorc = encerrada(c, 2)
        else:
            break
        turno = 0
    elif turno == 0:
        if errora == False and errorx == False:
            desplazamiento(a, 0)
            a = alteración(a, 0)
            errorx = encerrada(x, 0)
        elif errorb == False and errory == False:
            desplazamiento(b, 1)
            b = alteración(b, 1)
            errory = encerrada(y, 1)
        elif errorc == False and errorz == False:
            desplazamiento(c, 2)
            c = alteración(c, 2)
            errorz = encerrada(z, 2)
        elif errora == False:
            desplazamiento(a, 0)
            a = alteración(a, 0)
            errorx = encerrada(x, 0)
        elif errorb == False:
            desplazamiento(b, 1)
            b = alteración(b, 1)
            errory = encerrada(y, 1)
        elif errorc == False:
            desplazamiento(c, 2)
            c = alteración(c, 2)
            errorc = encerrada(z, 2)
        else:
            break
        turno = 1
    impr_tablero(tablero)
if errorx == True and errory == True and errorz == True:
    print("El jugador blanco no se puede mover, ha ganado el jugador negro")
elif errora == True and errorb == True and errorc == True:
    print("El jugador negro no se puede mover, ha ganado el jugador blanco")
