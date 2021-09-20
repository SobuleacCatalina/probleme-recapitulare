x=[1,2,3,4,5]
y=x
print('Suma primelor 3 componente ale lui x= ',x[0]+x[1]+x[2])
print('Suma tuturor componentelor variabilei y= ',sum(y))
p=1
for i in range(0,len(x)):
    p*=x[i]
print('Produsul tuturor componentelor variabilei x= ',p)
print('Valoarea absoluta a componentei a 3-a a variabilei y= ',abs(y[2]))
print('Suma primelor componente ale variabilelor x si y',x[0]+y[0])
