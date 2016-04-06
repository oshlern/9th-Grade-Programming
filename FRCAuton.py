import operator, re
form = ['rankingPoints', 'auto', 'challenge', 'goals', 'defense', 'record']
def openData(doc):
    text = open(doc, 'r')
    text = text.read()
    return text
def saveData(doc, data):
    output = open(doc,"w")
    output.write(data)
text = openData('FRCAuton')
text = re.sub(r'[0-9]*\s+([0-9]*)\s+([0-9]*)\.0\s+([0-9]*)\.0\s+([0-9]*)\.0\s+([0-9]*)\.0\s+([0-9]*)\.0\s+([0-9])-([0-9])-([0-9])\s+([0-9])\n', r'\1: [\2, \3, \4, \5, \6, \7, \8, \9], ', text)
text = '{' + text + '}'
saveData('FRCData', text)
# sortedPoints = sorted(points.items(), key=operator.itemgetter(1))
# for i in sortedPoints:
#     print i
#     print i[0]
