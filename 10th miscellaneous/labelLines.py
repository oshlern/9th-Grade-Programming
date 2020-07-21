def openData(doc):
    text = open(doc, 'r')
    text = text.read()
    return text

def saveData(doc, data):
    output = open(doc,"w")
    output.write(data)

def parse(doc):
    text = openData(doc)
    text = text.split('\n')
    if len(text[-1]) < 1:
        text.pop()
    for i in range(len(text)):
        line = str(i+1) + '  '
        if i < 10:
            line += '  '
        if line < 100:
            line += ' '
        text[i] = line + text[i]
    return '\n'.join(text)

print parse('WaitingRoom')
saveData('WaintingRoomParsed', parse('WaitingRoom'))
