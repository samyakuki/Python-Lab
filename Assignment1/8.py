import keyword

def is_valid_identifier(identifier):
    if not identifier:
        return False
    
    if identifier.startswith("_"):
        return False
    
    if identifier[0].isdigit():
        return False
    
    if identifier in keyword.kwlist:
        return False
    
    if not identifier.isidentifier():
        return False
    
    return True

userIdentifier = input("Enter the identifier: ")

if is_valid_identifier(userIdentifier):
    print("Valid")
else:
    print("Invalid")
