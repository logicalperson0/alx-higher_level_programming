#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = 0
    if len(sys.argv) == 1:
        print("{}".format(0))
    else:
        for i in range(1, len(sys.argv)):
            k = int(sys.argv[i])
            j = j + k
        print("{}".format(j))
