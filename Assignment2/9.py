test1 = int(input("Enter Test1 marks : "))
test2 = int(input("Enter Test2 marks : "))
test3 = int(input("Enter Test3 marks : "))
 
marks=[test1,test2,test3]
marks.sort()
print(f"Average of best 2 out of 3 is {(marks[1]+marks[2])/2}")