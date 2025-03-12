import os.path
import sys


def process_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            for i, line in enumerate(file, 1):
                print(f"{i}\t{line}", end='')
    else:
        print("Incorrect file path", end='')


def nl():
    args = sys.argv
    if len(args) > 1:
        for i in range(1, len(args)):
            print(f"File\t{args[i]}")
            process_file(args[i])
            print("\n")
    else:
        for i, line in enumerate(sys.stdin, 1):
            print(f"{i}\t{line}", end='')


if __name__ == "__main__":
    nl()
