from random import randint
def inmobil(f,c):
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

