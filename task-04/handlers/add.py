

def add_contact(args, contacts):
    name, phone = args

    if name in contacts.keys():
        return (f"ERROR: Contact {name} is already exist ")

    if phone in contacts.values():
        return (f"ERROR: Phone {phone} has another contact ")
    
    contacts[name] = phone
    return "Contact added."
     