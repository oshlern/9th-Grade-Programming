import numpy as np
import operator

teams = [100, 200, 300, 10,20,30]
kpa254 = 0.6
kpa971 = 0.2
# opr = {100: 10, 200: 23, 300: 4, 10: -10, 20: 20, 30: 15}
# ranking = [4904, 254]

# matches = [
# 	[[100,200,300],[10,20,30]],,
# 	[[100,20,30],[10,200,300]],
# ]

matches = [[[4270, 581, 5700], [5507, 3482, 668]],
[[2905, 1726, 6429], [971, 766, 604]],
[[5499, 6662, 2854], [4186, 6472, 2035]],
[[1458, 4990, 4973], [4904, 2437, 841]],
[[812, 6718, 5430], [6506, 1280, 3482]],
[[6429, 4270, 5419], [1700, 2035, 5499]],
[[766, 4990, 5700], [581, 5940, 1726]],
[[4973, 6718, 668], [6472, 6418, 4765]],
[[1458, 4159, 254], [971, 5507, 6662]],
[[2437, 812, 4669], [2905, 5924, 2854]],
[[841, 6036, 4186], [604, 1280, 4904]],
[[6506, 3256, 6418], [5026, 5700, 6429]],
[[581, 5419, 4990], [5924, 5499, 6718]],
[[6472, 4270, 1700], [4159, 2437, 1726]],
[[5430, 5026, 4186], [668, 971, 812]],
[[6506, 5507, 254], [766, 4973, 4904]],
[[1458, 604, 3482], [2035, 2854, 6036]],
[[1280, 6662, 841], [5940, 3256, 4765]],
[[2905, 5499, 766], [4669, 1700, 4159]]]
# \[\[(\d*), (\d*), (\d*), 
# [[$1, $2, \3], [

teams = []
for match in matches:
	for alliance in match:
		for team in alliance:
			if not team in teams:
				teams += [team]

rps = {}
for team in teams:
	rps[team] = 0 #or be given them already

opr = {254: 149.50, 581: 38.33, 604: 113.12, 668: 96.01, 766: 80.92, 812: 86.73, 841: 38.00, 971: 132.75, 1280: 31.38, 1458: 55.45, 1700: 64.53, 1726: 73.01, 2035: 75.41, 2437: -11.96, 2854: 15.77, 2905: 106.14, 3256: 166.33, 3482: 55.41, 4159: 99.16, 4186: 71.09, 4270: 47.00, 4669: 29.86, 4765: 68.09, 4904: 98.35, 4973: 37.63, 4990: 38.78, 5026: 61.02, 5419: 55.48, 5430: -16.97, 5499: 79.56, 5507: 64.36, 5700: 80.89, 5924: 30.08, 5940: 74.14, 6036: 82.41, 6418: 13.88, 6429: 27.76, 6472: 39.47, 6506: 46.40, 6662: 121.94, 6718: -4.69}
RPs = {254: [8, 20], 971: [7, 14], 6429: [7, 12], 3256: [8, 13], 6036: [8, 13], 6662: [7, 11], 2035: [7, 10], 4904: [7, 10], 1726: [7, 10], 604: [7, 9], 812: [7, 9], 2905: [7, 9], 5026: [8, 10], 1458: [7, 8], 5507: [7, 8], 4270: [7, 8], 6418: [8, 9], 5940: [8, 8], 5499: [6, 6], 841: [7, 7], 4669: [8, 7], 4765: [8, 7], 668: [7, 6], 4159: [7, 6], 5700: [7, 6], 4990: [7, 6], 3482: [7, 6], 4186: [7, 6], 1700: [7, 6], 4973: [7, 6], 1280: [7, 6], 5924: [8, 6], 5430: [8, 6], 581: [7, 5], 2437: [7, 5], 2854: [7, 4], 6506: [7, 4], 5419: [8, 4], 6472: [7, 3], 6718: [7, 2], 766: [6, 1]}
# RPS
# search  \d*	(\d*)	[\d|.]*	\d*	\d*	\d*	\d*	\d*	\d-\d-\d	\d	(\d)	(\d*)\n
# replace \1: [\2, \3], 
def play(match):
	red, blue = match[0], match[1]
	# print red, blue
	redOPR, blueOPR = sum([opr[team] for team in red]), sum([opr[team] for team in blue])
	print redOPR, blueOPR, [opr[team] for team in red], [opr[team] for team in blue]
	if redOPR > blueOPR:
		score = [2,0]
	elif redOPR < blueOPR:
		score = [0,2]
	else:
		score = [1,1]
	for i in range(2):
		if 254 in match[i]:
			if np.random.random() < kpa254:
				# print match
				score[i] += 1
		if 971 in match[i]:
			if np.random.random() < kpa971:
				# print 971, match
				score[i] += 1
	return score

def updateRPs():
	for matchNum in range(len(matches)):
		match, score = matches[matchNum], scores[matchNum]
		for alliance in range(len(match)):
			for team in match[alliance]:
				RPs[team][1] += score[alliance]
				RPs[team][0] += 1

def sortByScores(x):
	return sorted(x.items(), key=operator.itemgetter(1))

def sortByTeam(x):
	return sorted(x.items(), key=operator.itemgetter(0))

def randMatch():
	tempTeams = np.random.shuffle(teams)
	match = [teams[:3], teams[3:6]],
	return match

# print "opr", sortByScores(opr)
# print "teams", sorted(teams)

# for team in RPs:
# 	RPs[team] = np.true_divide(RPs[team][1], RPs[team][0])

# rps = sortByScores(RPs)
# RPs = {254: [8, 20], 971: [7, 14], 6429: [7, 12], 3256: [8, 13], 6036: [8, 13], 6662: [7, 11], 2035: [7, 10], 4904: [7, 10], 1726: [7, 10], 604: [7, 9], 812: [7, 9], 2905: [7, 9], 5026: [8, 10], 1458: [7, 8], 5507: [7, 8], 4270: [7, 8], 6418: [8, 9], 5940: [8, 8], 5499: [6, 6], 841: [7, 7], 4669: [8, 7], 4765: [8, 7], 668: [7, 6], 4159: [7, 6], 5700: [7, 6], 4990: [7, 6], 3482: [7, 6], 4186: [7, 6], 1700: [7, 6], 4973: [7, 6], 1280: [7, 6], 5924: [8, 6], 5430: [8, 6], 581: [7, 5], 2437: [7, 5], 2854: [7, 4], 6506: [7, 4], 5419: [8, 4], 6472: [7, 3], 6718: [7, 2], 766: [6, 1]}
# for i in range(len(rps)-1, -1, -1):
# 	print len(rps) - i, rps[i][0], rps[i][1]


# scores = [play(match) for match in matches]
# updateRPs()

for team in RPs:
	# RPs[team] = np.true_divide(RPs[team][1], RPs[team][0])
	RPs[team] = RPs[team][1]

print "rank, team, rps"
rps = sortByScores(RPs)
# for i in range(len(rps)-1, -1, -1):
# 	print len(rps) - i, rps[i][0], rps[i][1]

def playTeam(team):
	teamMatches = []
	for match in matches:
		for alliance in match:
			if team in alliance:
				teamMatches += [match]
	# teamMatches = [match for match in matches if team in match]
	for i in range(len(teamMatches)):
		print i, teamMatches[i], play(teamMatches[i])
# print play([[1458, 4990, 4973], [4904, 2437, 841]])

playTeam(971)

# print sorted(teams)




# for i in range(100):
# 	matches += [randMatch()]

# scores = [play(match) for match in matches]
# updateRPs()

