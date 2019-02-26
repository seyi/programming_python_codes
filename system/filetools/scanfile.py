
def scanner(file,function):
    with open(file,'r') as f:
        while 1:
            line = f.readline()
            if not line : break
            function(line)

        f.close() 

"""
    This version of scanner will improve speed and
    memory usage
"""

"""
def scanner(name,function):
    f = open(name,'r')
    for line in f.readlines() :
            function(line)
    f.close() 

"""

"""
Using file iterator fo scanning
"""

"""def scanner(name,function):
    with open(name,'r') as file:
        for line in file:
            function(line)
    file.close()
"""

"""
Using map instead of a for loop, a minalist version
"""

"""def scanner(name,function):
    map(function,open(name,'r'))
"""

"""
list comprehension
"""

def scanner(name,function):
    [function(line) for line in open(name,'r')]