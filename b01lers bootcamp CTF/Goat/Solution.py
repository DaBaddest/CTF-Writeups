randoms = [0,1,2,1,2,5,4,1,1,7,3,7,0,10,5,5,1,16,10,2,12,17]

final = [97,122,54,50,93,66,99,117,75,51,101,78,104,119,90,53,94,36,102,84,40,69]

ll=[]
for i, j in zip(randoms, final):
  ll.append(i^j)

mappings = [19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1]

a =[0 for i in range(22)]

for j,i in enumerate(mappings):
  a[i] = chr(ll[j])
print(''.join(a[::-1]))
