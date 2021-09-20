v=[1314,1122,885,1760,922,1582,1896]
print('Venit saptamanal= ',sum(v))
print('Media venitului zilnic= ',round(sum(v)/7,2))
zi=['luni','marti','miercuri','joi','vineri','sambata','duminica']
print('Ziua cu cel mai mare profit= ',zi[v.index(max(v))])
print('Ziua cu cel mai mic profit= ',zi[v.index(min(v))])