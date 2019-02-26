#!/usr/bin/python

######################################################
# Implement a web based interface for viewing/updating
# class instances stored in a shelve; shelve lives on
# server(same machine if localhost)
######################################################
import cgi,shelve


form = cgi.FieldStorage()
print "Content-type: text/html"
shelvename = 'class-shelve'
fieldnames = ('name','age','pay','job')

# Main html template
replyhtml = """
    <html>
        <title> People input form</title>
        <body>
            <form method=POST action="peoplecgi.py">
                 <table>
                    <tr> <th> Key</th> <td> <input type=text name=key value="%(key)s"> </input></td></tr>
                    $ROWS$
                </table>
             <p> 
                <input type=submit value="Fetch", name=action>
                <input type=submit value="Update", name=action>
             </p>
            </form>

        </body>
       
    </html>
"""

#insert Html for data rows at $ROWS$
rowhtml = '<tr> <th>%s </th><td> <input name=%s value="%%(%s)s"></td> </tr>'
rowshtml = ''

for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))

replyhtml = replyhtml.replace('$ROWS$',rowshtml)


def htmlize(dict):
    new = dict.copy()
    for field in fieldnames:
        value = new[field]
        new[field] = cgi.escape(repr(value))

    return new
def fetchRecord(db,form):
    try:
         key  = form['key'].value
         
         record =  db[key]
         fields = record.__dict__
         fields['key'] = key
    except :
        
        fields = dict.fromkeys(fieldnames,"?")
        fields['key'] = 'Missing or invalid key ' 

    return fields

def updateRecord(db,form):
        if not form.has_key ('key'):
            fields = dict.fromkeys(fieldnames,'?')
            fields['key'] = 'Missing key input'
        else:
            key = form['key'].value
            if key in db.keys():
                record = db[key]
            else:
                from person import Person
                record = Person(name='?',age='?')
            for field in fieldnames:
                setattr(record,field,eval(form[field].value))
            db[key] = record
            fields = record.__dict__
            fields['key'] = key
        return fields
#import sys
#sys.path.append('mymac/Users/eyitayofalana/Documents/GitHub/programming_python_codes')
#from dbret import db
import os
#os.chdir('/Users/eyitayofalana/Documents/GitHub/programming_python_codes')
db = shelve.open('class-shelve')
action = form.has_key('action') and form['action'].value

if action == 'Fetch':
    fields = fetchRecord(db,form)
elif action == 'Update':
    fields = updateRecord(db,form)
else:
    fields = dict.fromkeys(fieldnames,'?')
    fields['key'] = 'Missing or invalid action!'
db.close()
print replyhtml % htmlize(fields)


   
    


