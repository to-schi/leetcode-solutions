#solve with bash!

fhand = open('tenth-line.txt', 'r')

def tenthline():
    count = 0
    for line in fhand:
        count = count + 1
        if count == 10:
            return line

print(tenthline())
