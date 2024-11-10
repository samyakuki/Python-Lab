lst = [(15,6), (16,7), (16,8), (16,10), (17,13)]

print("The original list is: ")
print(lst)

res = []
for sub in lst:
   if res and res[-1][0] == sub[0]:
      res[-1].extend(sub[1:])
   else:
      res.append([ele for ele in sub])
res = list(map(tuple, res))

print("The joined list is: " )
print(res)