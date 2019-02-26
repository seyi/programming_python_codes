################################################################
#Save in-memory database object to a file with custom formatting
#assume 'endrec,','enddb.', and '=>' are not used in the data;
#assume db is dict of dict; warning eval can be dangerous- it
# runs string as code; could also eval() record dict at once
################################################################

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db,dbfilename=dbfilename) :
    "Formatted dump of database to flatfile"
    dbFile = open(dbfilename,'w')
    for key in db :
        print >>dbFile, key
        for(name,value) in db[key].items():
            print>>dbFile, name + RECSEP + repr(value)
        print >>dbFile,ENDREC
    print >>dbFile ,ENDDB
    dbFile.close()


def loadDatabase(dbfilename=dbfilename) :
    "Parse data to reconstruct database"
    dbFile = open(dbfilename)
    import sys
    sys.stdin = dbFile
    db = {}
    key = raw_input()
    while key != ENDDB:
        rec  = {}
        field = raw_input()
        while field != ENDREC:
            name,value =field.split(RECSEP)
            rec[name]  = eval(value)
            field = raw_input()
        db[key]  = rec
        key = raw_input()
    return db

if __name__ == "__main__":
    from initdata import db
    print('PRINTING DB', db)
    storeDbase(db)