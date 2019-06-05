
exports.method = function(turnNumber, opponentsMoves, yourMoves){
  var first = 0.95;
  var second = 0.6;
  var totalTurnNum = 20;
  if (turnNumber >= totalTurnNum) {
    return false;
  }
  if (turnNumber <= 1) {
    return (Math.random() < first);
  }
  if (turnNumber === 2) {
    if (opponentsMoves[0]) {
      return true;
    }
    return (Math.random() < second);
  }
  if (turnNumber === 3) {
    return opponentsMoves[1];
  }
  if (opponentsMoves[-1]===yourMoves[-2]) {
    if (turnNumber > 4 && -2 != -3) {
      return false;
    } 
    return opponentsMoves[-1];
  }
  return false;
};
// fix last elements of the list
// make one long thing with ands and ors
