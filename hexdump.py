import sys


def binaryToHex(bytes: bytearray) -> str:
    """convert the given bytes
    to hex representation
    """
    result = ""
    for i in range(0, len(bytes), 1):
        if (i == 8):
            result += " "
        result += " " + f"{bytes[i]:02x}"
    return result


def showCounter(lineNumber: int) -> str:
    """return the base 16
    counter for where in the file
    we are
    """
    return f"{lineNumber:08x}"


def pipeRepresent(bytes: bytearray) -> str:
    """represent the given bytes
    in ascii where printable, otherwise
    show a '.'
    """
    result = "|"
    for i in bytes:
        if (ord(chr(i)) >= 32 and ord(chr(i)) <= 126):
            result += chr(i)
        else:
            result += "."
    return result + "|"


def main():
    row = 0
    with open(sys.argv[1], 'rb') as filedes:
        middleCol = filedes.read(16)
        if (len(middleCol) < 1):
            exit()
        while len(middleCol) == 16:
            print(showCounter(row*16) + " " + f"{binaryToHex(middleCol):<48}" +
                  "  " + f"{pipeRepresent(middleCol)}")
            row += 1
            middleCol = filedes.read(16)
        if (len(middleCol) > 0):
            print(showCounter(row*16) + " " + f"{binaryToHex(middleCol):<49}" +
                  "  " + f"{pipeRepresent(middleCol)}")
        print(showCounter(((row)*16) + len(middleCol)))


if __name__ == "__main__":
    main()
