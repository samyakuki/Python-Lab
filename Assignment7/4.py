from functools import reduce

students = [
    {'name': 'Alice', 'score': 45},
    {'name': 'Bob', 'score': 55},
    {'name': 'Charlie', 'score': 65},
    {'name': 'David', 'score': 75}
]

morethan50=filter(lambda x:x["score"]>50,students)

nameoffiltered=list(map(lambda x:x["name"],morethan50))

total_score = reduce(lambda acc, x: acc + x["score"], students, 0)
average_score = total_score / len(students)

print(nameoffiltered,average_score)