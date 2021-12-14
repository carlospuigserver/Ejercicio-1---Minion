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
    
