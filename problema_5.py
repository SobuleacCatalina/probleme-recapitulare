x=[1,2,3,4,5]
y=x
print(x[0]+x[1]+x[2])
print(sum(y))
p=1
for i in range(0,len(x)):
    p*=x[i]
print(p)
print(abs(y[2]))
print(x[0]+y[0])