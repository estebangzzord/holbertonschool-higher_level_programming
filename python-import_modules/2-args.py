#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{}.".format(i), end='')
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
