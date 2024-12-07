


def show_phone(args, contacts):
    for key, value in contacts.items():
        if key == args[0]:
            print(f"Result \n>>> {key}: {value}")
            break
        print(f"There's no phone {args[0]} in contacts")