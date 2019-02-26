import pickle, glob

for filename in glob.glob('*.pkl'):
    recfile = open(filename)
    record = pickle.load(recfile)
    print filename, '=>\n',record

suefile = open('sue.pkl')
print pickle.load(suefile)['name']