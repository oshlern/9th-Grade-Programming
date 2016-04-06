import operator
chems = {'Ni': 1.91, 'Cu': 1.90, 'Fe': 1.83, 'Zn': 1.65, 'Al': 1.61, 'Mn': 1.55, 'Mg': 1.31}
diffs = {}
for i in range(len(chems)-1):
    chem1 = chems.keys()[i]
    for j in range(i+1, len(chems)):
        chem2 = chems.keys()[j]
        diffs[chem1+chem2] = int(round((100*(chems[chem1]-chems[chem2]))))
diffs = sorted(diffs.items(), key=operator.itemgetter(1))
print diffs
print len(diffs)
