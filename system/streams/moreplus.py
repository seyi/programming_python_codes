####################################################
# Split and interactively page a string, file, 
# or stream of text to stdout; When run as a 
# script,page stdin or file whose name is passed
# on cmdline, if input is stdin, can't use it 
# for user reply--use platform specific tools or GUI
####################################################
import sys
def getreply():
    """
    read a reply key from an ineractie use
    even if stdin is redirected to a pipe or file
    """

    if sys.stdin.isatty():
        return raw_input('?')
    else:
        if sys.platform[:3] == 'win':
            import msvcrt
            msvcrt.putch('?')
            key = msvcrt.getche()
            msvcrt.putch('\n')
            return key
        elif sys.platform[:5] == 'linux' or sys.platform[:6] == 'darwin':
            print '?'
            console = open('/dev/tty')
            line = console.readline()[:-1]
            return line
        else:
            print '[pause]'
            import time
            time.sleep(5)
            return 'y'

def more(text,numlines=10):
    """
    split multiline string to stdout
    """
    lines = text.split('\n')
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk : print line
        if lines and getreply() not in ['y','Y'] : break

if __name__ == "__main__":
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())