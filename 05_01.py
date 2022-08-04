numero=0
total=0.0
#LOOP infinito hasta decir basta (break)
while True:
    nro=input('introduzca nro: ')
    if nro=='basta':
        break
#por si no es nro try except
    try:
        valor=float(nro)
    except:
        print('no es nro')
        continue
#conteo
    numero=numero+1
#suma
    total=total+valor
print(total,numero,total/numero)
