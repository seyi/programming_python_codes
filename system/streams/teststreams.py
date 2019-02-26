
# Read numbers till end of file and show squares
import sys
def interact():
    print 'Hello stream world!'
    while 1:
        try:
            reply = raw_input('Enter number>>>')
        except EOFError:
            break
        else:
            num = int(reply)
            #print sys.stdin.readline()[:-1]
            print 'the square of %d is %d' % (num,num*num)
    print 'Bye'

    
    
if __name__ == '__main__':
    interact()