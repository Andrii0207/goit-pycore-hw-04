

def show_all(_, contacts):
    
    if not len(contacts.keys()):
        return print("Oops, contacts is empty")
    
    print("Contacts:")
    print(f"\t{contacts}")