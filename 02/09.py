boris = int(input())
vova = int(input())
dima = int(input())

if boris < vova:
    boris, vova = vova, boris
if vova < dima:
    vova, dima = dima, vova
if boris < vova:
    boris, vova = vova, boris
    
print(boris, vova, dima)