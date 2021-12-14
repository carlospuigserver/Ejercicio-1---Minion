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

    #posicionpiezas
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
