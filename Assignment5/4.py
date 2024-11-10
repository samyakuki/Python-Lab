emails=[
    "alex@gmail.com",
    "lily@gmail.com",
    "rexford@gmail.com"
    "rexford@gmail.com"
    "luke@gmail.com",
    "hailey@gmail.com",
    "manny@gmail.com",
    "manny@gmail.com",
    "joe@gmailcom",
    "joe@gmailcom",
    "rexford@gmail.com"
    "rexford@gmail.com"
]

seen=set()
duplicates=set()
for email in emails:
    if email in seen:
        duplicates.add(email)
    else:
        seen.add(email)
print("Duplicate emails : ",sorted(duplicates))            