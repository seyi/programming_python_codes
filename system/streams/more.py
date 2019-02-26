######################################################
# Split or interactively page a string or file of text
######################################################

def more(text,numlines=15):
    lines = text.split('\n')
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk : print line
        if lines and raw_input('More?') not in ['y','Y']:
            break

if __name__ == '__main__':
    import sys
    #more(open(sys.argv[0]).read(),10)
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())
