#!/usr/bin/env python
from sys import argv
from scanfile import scanner
class UnknownCommand(Exception): pass

commands = {'*':'Mrs','+':'Mr'} # Data is easier to expand than code

""" def processLine(line):
    if line[0] == '*':
        print 'Hello Mrs ', line[1:-1]
    elif line[0] == '+' :
        print 'Hello Mr ', line[1:-1]
    else:
        raise UnknownCommand, line 
 """

def processLine(line):
     try:
         print 'Hello ', commands[line[0]] , ' ', line[1:-1]
     except KeyError:
         raise UnknownCommand, line




filename = 'data.txt'



if len(argv) == 2: filename = argv[1]

scanner(filename,processLine)


