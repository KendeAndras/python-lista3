summ=0
sumList=[]
for i in range(1,101):
    if i%3!=0 and '3' not in str(i):
        print(i, "end," )
        summ+=1
        sumList.append(i)

print(summ)
print(sumList)
print(sum(sumList))
print(max(sumList))
