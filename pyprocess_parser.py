import sys
print sys.argv[1]
f= open(sys.argv[1], "r")

lines=f.readlines()

a = eval(lines[9][19:])
b = eval(lines[11][15:])

print a
print b

f.close()
