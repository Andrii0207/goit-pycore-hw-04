from parser import parse_input
from handlers import add, all, change, show, delete


def main():
    print("Welcome to the assistant bot!")

    contacts = {"John": "0987654321"}

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
 
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add.add_contact(args, contacts))
        elif command == "change":
            print(change.change_contact(args, contacts))
        elif command == "phone":
            print(show.show_phone(args, contacts))
        elif command == "all":
            print(all.show_all(args, contacts))
        elif command == "delete":
            print(delete.delete_contact(args, contacts))
        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()
