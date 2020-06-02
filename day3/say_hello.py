import sys

arg1 = sys.argv[0]
arg2 = ""

if len(sys.argv) == 1:
    pass
else:
    arg2 = sys.argv[1]


if arg2 == "--shout":
    print("HELLO THERE!")
else:
    print("Hello, there")
