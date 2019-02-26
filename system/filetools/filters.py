def filter_files(name,function):
    input = open(name,'r')
    output = open(name+'.out','w')

    for line in input.readlines():
        output.write(function(line))
    input.close()
    output.close()

def  filter_stream(function):
    import sys
    while 1:
        line = sys.stdin.readline()
        if not line : break
        print function(line),

if __name__ == '__main__':
    filter_stream(lambda line : line[:4]+'***'+line[4:-1]+'\n')
    filter_files('hillbillies.txt',
                    lambda line : 
                        if line[1:-1] == 'Granny': line)