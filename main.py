from pathlib import Path
import os

def create_file():
    try:
        name = input("enter your file name: ")
        path = Path(name)
        if not path.exists():
            with open(path, 'w') as f:
                data = input("enter data to write in file: ")
                f.write(data)
                print("file created successfully: ")
        else:
            print("Error File name already exists")
    except Exception as err:
        print(f"an error occured as {err}")

def read_file():
    try:
        name = input("enter your file name: ")
        path = Path(name)
        if path.exists():
            with open(path, 'r') as f:
                content = f.read()
                print(content)
        else:
            print("error no such file exists")
    except Exception as err:
        print(f"an error occured as {err}")

def update_file():
    try:
        name = input("enter the file name: ")
        path = Path(name)
        if path.exists():
            choice = int(input("Enter 1 to rename the file: \nEnter 2 to append into file: \nEnter 3 to overwrite the file: "))

            if choice == 1:
                newname = input("Enter new file name: ")
                newpath = Path(newname)
                if not newpath.exists():
                    path.rename(newpath)
                    print("file renamed successfully: ")
                else:
                    print("file with new name already exists.")

            elif choice == 2:
                with open(path, 'a') as f:
                    data = input("enter information to append: ")
                    f.write(data)
                    print("information appended successfully: ")

            elif choice == 3:
                with open(path, 'w') as f:
                    data = input("enter information to overwrite: ")
                    f.write(data)
                    print("file overwritten successfully: ")

    except Exception as err:
        print(f"an error occured {err}")


def delete_file():
    try:
        name = input("please tell your file name :- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("file deleted successfully")
        else:
            print("Error no such file exists")
    except Exception as err:
        print(f"An error occured as {err}")


choice = int(input("Enter 1 for creating File \nEnter 2 for reading the file \nEnter 3 for updating the file \nEnter 4 for deleting file "))

match choice:
    case 1:
        create_file()
    case 2:
        read_file()
    case 3:
        update_file()
    case 4:
        delete_file()
    case _:
        print("invalid choice")
