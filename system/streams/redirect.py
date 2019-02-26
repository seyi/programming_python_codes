####################################################
# File like object that save standard output text
# in a string and provide standard input text from
# a string; redirect runs a passed in function with
# it's output and input streams reset to these file
# like class objects
####################################################


import sys

class Output:
    def __init__(self):
        self.text = ''
    def write(self,string):
        self.text = self.text + string
    def writeLines(self,lines):
        for line in lines: self.write(line)

class Input:
    def __init__(self,input=''):
        self.text = input
    def read(self,*size):
        if not size:
            res,self.text = self.text,''
        else:
            res,self.text = self.text[:size[0]],self.text[size[0]:]
        return res

    def readline(self):
        eoln = self.text.find('\n')
        if eoln != -1 :
            res, self.text = self.text[:eoln+1], self.text[eoln+1:]
        else:
            res, self.text = self.text,''
        return res

def redirect(function,args,input):
    
    savestream = sys.stdout,sys.stdin
    sys.stdout = Output()
    sys.stdin = Input(input)

    try:
        function(*args)
    except:
        sys.stderr.write('error in function!')
        sys.stderr.write('%s %s \n' % tuple(sys.exc_info()[:2]))

    result = sys.stdout.text

    sys.stdout,sys.stdin = savestream

    return result
                    