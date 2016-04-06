// Set paramaters
strokeWeight(0.3);
var backcolor = color(200, 235, 235);
var maxlength = 500;
var Slength = 0;
var Scolor1 = color(10, 122, 10);
var Scolor2 = color(205, 217, 35);
var Ssize = 10;
var Sstroke = color(0,0,0);
var width2 = 1;
var nowdirection = "none";
var die = 0;
var num = 0;
var numDiff=0.15;
var x = 0;
var z = 0;
var specialCherry = 0;
var specialCherryProbability = 7;
var specialCherryBonus = 5;
var cherryBonus = 1;
var cherryX = -10;
var cherryY = -10;
var cherry = 0;
var badCherriesNum = 0;
var maxBadCherries = 10;
var badCherryProbability = 100;
keyCode=0;
maxBadCherries-=1;
// Set initial position
var Sx = Array(maxlength);
var Sy = Array(maxlength);
var badCherryX = Array(maxBadCherries);
var badCherryY = Array(maxBadCherries);
for (var index=0; index<maxlength; index++) {
    Sx[index]=-10;
    Sy[index]=-10;
    badCherryX[index]=-10;
    badCherryY[index]=-10;
}
Sx[0]=1;
Sy[0]=1;

var backg = function() {
    strokeWeight(4);
    fill(backcolor);
    stroke(209, 50, 50);
    rect(1,1,398,398);
    strokeWeight(0.3);
    for (var i=4; i<400; i+=Ssize) {
        line(i,0,i,400);
    }
    for (var j=4; j<400; j+=Ssize) {
        line(0,j,400,j);
    }
};

var drawSnake = function(index) {
    fill(Scolor2);
    stroke(Sstroke);
    rect(Sx[index]*Ssize+4,Sy[index]*Ssize+4,Ssize,Ssize);
    fill(Scolor1);
    noStroke();
    rect(Sx[index]*Ssize+4+width2,Sy[index]*Ssize+4+width2,Ssize-(2*width2),Ssize-(2*width2));
};

var moveFront = function() {
    if (nowdirection==="right") {
        Sx[0]++;
    }
    if (nowdirection==="left") {
        Sx[0]-=1;
    }
    if (nowdirection==="up") {
        Sy[0]-=1;
    }
    if (nowdirection==="down") {
        Sy[0]++;
    }
};

var moveSnake = function(index) {
    Sx[index]=Sx[index-1];
    Sy[index]=Sy[index-1];
};

var runIn= function(index) {
    for (x=0; x<=Slength; x++) {
        if (x!==index && Sx[index]===Sx[x] && Sy[index]===Sy[x]) {
            die=1;
        }
    }
};

var setDirections = function() {
    if (nowdirection==="up" || nowdirection==="down" || nowdirection==="none") {
        if (keyCode===RIGHT) {
            nowdirection="right";
        }
        if (keyCode===LEFT) {
            nowdirection="left";
        }
    }
    if (nowdirection==="right" || nowdirection==="left" || nowdirection==="none") {
        if (keyCode===UP) {
            nowdirection="up";
        }
        if (keyCode===DOWN) {
            nowdirection="down";
        }
    }
};

var offScreen = function() {
    if (Sx[0]>=round(390/Ssize) || Sx[0]<0 || Sy[0]>round(390/Ssize) || Sy[0]<0) {
        die=1;
    }
};

var tesselate = function() {
    if (Sx[0]>=round(385/Ssize)) {
        Sx[0]=0;
    }
    if (Sx[0]<0) {
        Sx[0]=round(380/Ssize);
    }
    if (Sy[0]>=round(385/Ssize)) {
        Sy[0]=0;
    }
    if (Sy[0]<0) {
        Sy[0]=round(385/Ssize);
    }
};

var drawCherry = function() {
    stroke(255,150,150);
    strokeWeight(2.5);
    fill(255,0,8);
    if (specialCherry===1) {
        stroke(178, 184, 18);
        fill(242, 220, 19);
    }
    ellipse((cherryX+1/2)*Ssize+4, (cherryY+1/2)*Ssize+4,Ssize,Ssize);
    strokeWeight(0.3);
};

var createCherry= function() {
    cherryX=round(random(380/Ssize));
    cherryY=round(random(380/Ssize));
    if (random(specialCherryProbability)<=1) {
        specialCherry=1;
    }
};

var eatCherry = function() {
    if (Sx[0]===cherryX && Sy[0]===cherryY) {
        Slength+=cherryBonus;
        if (specialCherry===1) {
            Slength+=specialCherryBonus-1;
            numDiff+=(specialCherryBonus-1)/70;
            //numDiff=numDiff*2;
            specialCherry=0;
        }
        createCherry();
        numDiff+=1/70;
    }
};

var drawBadCherries = function() {
    for (index=0; index<=maxBadCherries; index++) {
        if (badCherryX[index]!==-10) {
            stroke(31, 56, 219);
            strokeWeight(2.5);
            fill(56, 175, 240);
            ellipse((badCherryX[index]+1/2)*Ssize+4, (badCherryY[index]+1/2)*Ssize+4,Ssize,Ssize);
            strokeWeight(0.3);
        }
    }
};

var createBadCherry= function() {
    if (nowdirection!=="none") {
        if (random(badCherryProbability)<=1) {
            badCherryX[floor(random(10)+0.5)]=round(random(385/Ssize));
            badCherryY[floor(random(10)+0.5)]=round(random(385/Ssize));
            badCherriesNum++;
        }
    }
};

var eatBadCherry = function() {
    for (index=0; index<=maxBadCherries; index++) {
        if (Sx[0]===badCherryX[index] && Sy[0]===badCherryY[index]) {
            Slength-=1;
            numDiff-=0.02;
            badCherryX[index]=-10;
            badCherryY[index]=-10;
            badCherriesNum-=1;
            if (Slength<0) {
                die=1;
            }
        }
    }
};

var death = function() {
    if (die===1) {
        for (index=0; index<maxlength; index++) {
            Sx[index]=-10;
            Sy[index]=-10;
        }
        for (index=0; index<maxBadCherries; index++) {
            badCherryX[index]=-10;
            badCherryX[index]=-10;
        }
        Sx[0]=1;
        Sy[0]=1;
        badCherriesNum=0;
        Slength=0;
        nowdirection = "none";
        numDiff=0.15;
        specialCherry=0;
        createCherry();
        keyCode=0;
        die = 0;
    }
};

// The Game
createCherry();
var draw = function() {
    if (num>=1) {
        backg();
        drawCherry();
        drawBadCherries();
        for (var index=0; index<=Slength; index++) {
            drawSnake(index);
            runIn(index);
        }
        for (index=maxlength-1; index>0; index-=1) {
            moveSnake(index);
        }
        moveFront();
        createBadCherry();
        eatBadCherry();
        eatCherry();
        tesselate();
        death();
        //offScreen();
        num=0;
    }
    else {
        num+=numDiff;
    }
    setDirections();
};
