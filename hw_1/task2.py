import os.path
import sys


def process_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            for line in file.readlines()[-10:]:
                print(line, end='')
    else:
        print("Incorrect file path")


def tail():
    args = sys.argv
    if len(args) > 1:
        for i in range(1, len(args)):
            print(f"==> {args[i]} <==")
            process_file(args[i])
            print("\n")
    else:
        for line in sys.stdin.readlines()[-17:]:
            print(line, end='')


if __name__ == "__main__":
    tail()