liste = [1,5,11,7,9,2,6,4,10,3,8]
result= set()
pick = int(input("pick a number: "))
j=0
for i in liste:
    if (i<pick) : 
        to_find = pick-i
        if ((i+to_find == pick)) :
            result.add((i,to_find,liste.index(i),liste.index(to_find)))
print(result)

