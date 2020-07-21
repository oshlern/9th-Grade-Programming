people = ['osher', 'shaheen', 'nico']
types = ['question', 'answer', 'retort']
#represent [person, [type0, type2] or [person, type0], [person, type2]
conversation = [[people[0], types[0]], []]

def record():
    inputs = []

def analyze(conversation, people, types):
    ps = {}
    ts = {}
    for t in types:
        ts[t] = {}
    for person in people:
        ps[person] = {}
        for t in types:
            ps[person][t] = 0
            ts[t][person] = 0
    for segment in conversation:
        ps[segment[0]][segment[1]] += 1
        ts[segment[1]][segment[0]] += 1
    return ps, ts

#http://spacy.io/
