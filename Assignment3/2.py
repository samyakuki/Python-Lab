birthdays = {
"A": "16-06-2003",
"S": "11-09-2004",
"B": "30-06-2004",
"0": "20-05-2004"
}
name = input("Enter the name to find the birthday: ")
if name in birthdays:
    birthdate = birthdays[name]
    birthdate_parts = birthdate.split("-")
    formatted_birthdate = "/".join(birthdate_parts)
    print(f"{name}'s birthday is on {formatted_birthdate}")
else:
    print("No birthday found for",name)