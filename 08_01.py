abrir = open('mbox-short.txt')

for line in abrir:
    line = line.rstrip()
    #transformar en lista
    wds = line.split()
#para evitar error de renglones en blanco (guardian patern) 3 porque me interesa la 3er palabra
    if len(wds) < 3:
        continue
#elegir renglones "from"
    if wds[0]!='From' :
        continue
    print(wds[2])
