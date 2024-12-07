import sys
from pathlib import Path, PurePath
from colorama import Fore, Back, Style


def parse_folder(directory):

    for element in directory.iterdir(): 
        if element.is_dir():
            print(Fore.BLUE + f"Folder 📂 {element}/")
            parse_folder(element)
        else:
            print(Fore.GREEN + f"\tfile 📄 {element.name}")
    
    print(Style.RESET_ALL)
    


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage:  python3 main.py images")
        print("\tpython3 main.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    directory = Path(folder_path)

    if not directory.exists():
        print(Back.RED + "Entered folder not exist. Please enter folder as argument" + Style.RESET_ALL)
        sys.exit()
    
    if not directory.is_dir():
        print(Back.YELLOW + "Entered data is not a directory. Please enter directory name as argument" + Style.RESET_ALL)
        sys.exit()

    parse_folder(directory)