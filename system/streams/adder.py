
import sys
sum = 0

while True:
    try:
        line = raw_input()
    except EOFError:
        break
    else:
        sum += int(line)

print sum