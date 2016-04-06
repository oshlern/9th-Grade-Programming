import operator
data = {20: [112, 80, 152, 290, 6, 0, 0], 18: [114, 60, 88, 295, 6, 0, 0], 16: [154, 75, 143, 290, 5, 1, 0], 16: [138, 75, 218, 245, 4, 1, 0], 15: [114, 60, 129, 285, 5, 1, 0], 14: [128, 70, 119, 235, 5, 0, 0], 13: [152, 65, 89, 310, 3, 2, 1], 13: [128, 50, 182, 245, 3, 1, 1], 13: [114, 40, 100, 260, 4, 1, 0], 13: [110, 65, 79, 270, 4, 2, 0], 13: [100, 100, 80, 275, 4, 2, 0], 13: [76, 70, 109, 245, 4, 2, 0], 12: [106, 60, 38, 290, 4, 2, 0], 12: [100, 50, 21, 295, 4, 2, 0], 12: [94, 40, 44, 230, 4, 1, 0], 12: [92, 45, 49, 240, 4, 1, 0], 12: [82, 40, 66, 230, 4, 1, 0], 11: [146, 65, 74, 290, 3, 2, 1], 11: [130, 65, 90, 290, 3, 3, 0], 11: [106, 70, 60, 270, 3, 3, 0], 11: [96, 65, 146, 220, 3, 1, 1], 11: [58, 55, 53, 250, 3, 3, 0], 10: [102, 35, 49, 245, 4, 2, 0], 10: [82, 55, 99, 270, 3, 3, 0], 10: [72, 65, 38, 230, 3, 2, 0], 10: [68, 60, 32, 250, 3, 3, 0], 9: [116, 40, 102, 255, 3, 3, 0], 9: [106, 25, 49, 215, 3, 2, 0], 9: [96, 45, 31, 250, 3, 3, 0], 9: [90, 60, 37, 275, 3, 3, 0], 9: [90, 55, 90, 205, 3, 2, 0], 9: [74, 35, 25, 225, 3, 2, 0], 9: [68, 50, 55, 265, 2, 4, 0], 9: [62, 65, 34, 260, 2, 4, 0], 8: [102, 50, 50, 210, 3, 2, 0], 8: [88, 50, 31, 295, 1, 4, 1], 8: [86, 40, 45, 245, 3, 3, 0], 8: [78, 40, 79, 200, 3, 2, 0], 8: [74, 25, 23, 235, 3, 3, 0], 8: [70, 40, 64, 260, 2, 4, 0], 7: [84, 70, 53, 275, 1, 5, 0], 7: [82, 50, 82, 200, 2, 3, 0], 7: [82, 50, 51, 200, 2, 3, 0], 7: [82, 35, 62, 195, 2, 2, 1], 7: [62, 40, 41, 205, 2, 3, 0], 7: [60, 35, 72, 220, 3, 3, 0], 7: [56, 50, 16, 210, 2, 3, 0], 6: [108, 60, 57, 300, 1, 5, 0], 6: [92, 50, 35, 280, 1, 5, 0], 6: [76, 40, 38, 255, 2, 4, 0], 6: [72, 20, 50, 165, 2, 2, 0], 5: [78, 40, 41, 205, 2, 4, 0], 5: [70, 40, 53, 240, 1, 5, 0], 5: [54, 50, 74, 225, 1, 5, 0], 4: [66, 25, 6, 190, 1, 4, 0], 3: [46, 40, 22, 200, 1, 5, 0], 2: [66, 40, 47, 180, 0, 5, 0], 1: [54, 30, 26, 180, 0, 5, 0], 0: [50, 25, 19, 155, 0, 4, 0], 0: [48, 20, 24, 150, 0, 5, 0]}
form = ['rankingPoints', 'auto', 'challenge', 'goals', 'defense', 'win', 'lose', 'draw']
sortedData = sorted(data.items(), key=operator.itemgetter(1))
for i in sortedData:
    print i