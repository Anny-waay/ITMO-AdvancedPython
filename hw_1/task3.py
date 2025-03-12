import os.path
import sys


def process_text(text, file_name=None):
    lines = text.count('\n')
    words = len(text.split())
    bytes = len(text.encode("utf-8"))

    print(f"{lines} {words} {bytes}" + (f" {file_name}" if file_name else ""))

    return lines, words, bytes


def wc():
    args = sys.argv
    if len(args) == 2:
        if os.path.isfile(args[1]):
            with open(args[1], "r") as file:
                process_text(file.read(), args[1])
    elif len(args) > 2:
        all_lines, all_words, all_bytes = 0, 0, 0
        for i in range(1, len(args)):
            if os.path.isfile(args[i]):
                with open(args[i], "r") as file:
                    lines, words, bytes = process_text(file.read(), args[i])
                    all_lines += lines
                    all_words += words
                    all_bytes += bytes
        print(f"{all_lines} {all_words} {all_bytes} итого")
    else:
        process_text(sys.stdin.read())


if __name__ == "__main__":
    wc()