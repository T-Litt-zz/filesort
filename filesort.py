from os import listdir, mkdir
from os.path import isdir, isfile, join, exists
from shutil import move


def main():
    while True:
        while True:
            print("Welcome to file sorter: 0) Quit    1) Sort by title    2) Sort by format")
            mode = input("Mode: ")
            try:
                mode = int(mode)
                break
            except ValueError:
                print("Input of mode must be integer! Please try again! \n")
        if mode == 0:
            print("Thank you for using this program!")
            break
        elif (mode == 1) or (mode == 2):
            while True:
                path = input("Enter the directory: ")
                if isdir(path):
                    files = (f for f in listdir(path) if isfile(join(path, f)))
                    for file in files:
                        directory = join(path, file.split(".")[int(mode) - 1])
                        if not exists(directory):
                            mkdir(directory)
                        move(join(path, file), directory)
                    print("Operation Complete! \n")
                    break
                else:
                    print("Invalid input! Please try again!")
        else:
            print("Invalid option! Please try again! \n")


main()
