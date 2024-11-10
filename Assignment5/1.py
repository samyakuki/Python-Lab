s1=[101, 102, 103, 104, 105]
s2= [103, 104, 106, 107, 108]
set1=set(s1)
set2=set(s2)
symmetric_diff=set1.symmetric_difference(set2)
print(symmetric_diff)