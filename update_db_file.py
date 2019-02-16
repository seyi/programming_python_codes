from make_db_files import loadDatabase, storeDbase

db = loadDatabase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

storeDbase(db)