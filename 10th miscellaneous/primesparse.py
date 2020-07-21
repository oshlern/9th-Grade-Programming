import re
def openData(doc):
    text = open(doc, 'r')
    text = text.read()
    return text

def saveData(doc, data):
    text = open(doc, 'w')
    text = text.write(data)

def parse(doc):
    text = openData(doc)
    text = re.sub(r'\s', '', text)
    return text

saveData('primesParsed',parse('primes'))
