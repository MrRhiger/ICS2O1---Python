list1 = [13,25,-8,52,17,-15]
list2 = [-12,56,-98,123,47,2]
total = []

for x in range(len(list1)):
    total.append(list1[x] + list2[x])
    

for y in total:
    print(y, end =" ")
