// exports.method = function(currentRound, opHistory, myHistory) {
//     if (currentRound <= 1) {return (math.random(0,1)>0.5);}
//     var avg = array.reduce(function(pv, cv) { return pv + cv; }, 0)/(currentRound-1);
//     return (avg>0.5);
// };
exports.method = function(currentRound, opHistory, myHistory) {
    if (currentRound <= 1) {return true;}//(math.random()>0.5);}
    var sum = 0;
    for (var i=0; i<currentRound-1; i++) {sum += opHistory[i];}
    return (sum/(currentRound-1)>0.5);
};
