background(228, 153, 240);
angleMode = "degrees";
var pi=3.1415926535897932384626433832795028841971693993751;
var R=380000000;
var volume=400*400;
var gravity={direction:270, strength:0};
var friction=0;
var pressure=0;
var pressures=500;
var collisions=[];
for (var i=0;i<pressures;i++){
    collisions[i]=0;
}
var timer=0;

//mv1+mv2=mv1'+mv2' momentum is conserved
//mv1^2+mv2^2=mv1'^2+mv2'^2 kinetic energy is conserved

//object to object gravity, orbitals (gravity=0,distance and mass (cosine and sine))
//display KE and PE

//PE: (distance from the edge *sec or csc gravity_angle)

//display center of mass

var backg=function(){
    background(228, 153, 240);
};
var balls=[];
var newBall = function(x,y,siz,color){
    var density=1;
    balls.push(
    {x:x,
    y:y,
    siz:siz,
    density:density,
    mass:siz*siz*density,
    color:color,
    xv:0,
    yv:0,
    direction:0,
    speed:0
    });
};

var drawBalls = function(){
    for (var i=0;i<balls.length;i++){
        fill(balls[i].color);
        ellipse(balls[i].x,400-balls[i].y,balls[i].siz,balls[i].siz);
    }
};

var bounce = function(ball){
    if (ball.x+ball.siz/2>400){
        ball.x=400-ball.siz/2;
        collisions[timer]+=ball.mass*ball.xv;
        ball.xv=-(abs(ball.xv)-friction);
        // if (ball.xv>-0.3){
        //     ball.xv=-0.3;
        // }
    }
    if (ball.x-ball.siz/2<0){
        ball.x=0+ball.siz/2;
        collisions[timer]-=ball.mass*ball.xv;
        ball.xv=abs(ball.xv)-friction;
        // if (ball.xv<0.3){
        //     ball.xv=0.3;
        // }
    }
    if (ball.y+ball.siz/2>400){
        ball.y=400-ball.siz/2;
        collisions[timer]+=ball.mass*ball.yv;
        ball.yv=-(abs(ball.yv)-friction);
        // if (ball.yv>-0.3){
        //     ball.yv=-0.3;
        // }
    }
    if (ball.y-ball.siz/2<0){
        ball.y=0+ball.siz/2;
        collisions[timer]-=ball.mass*ball.xv;
        ball.yv=abs(ball.yv)-friction;
        // if (ball.yv<0.3){
        //     ball.yv=0.3;
        // }
    }
};

var collide=[];
var collision=function(j){
    var ball1=balls[j];
    for (var i=0;i<balls.length;i++){
        if (balls[i]!==ball1){
            if (collide[j][i]===0&&collide[i][j]===0){
                if (sqrt(pow((balls[i].x-ball1.x),2)+pow((balls[i].y-ball1.y),2))<=(balls[i].siz/2+ball1.siz/2)){
                    var ball2=balls[i];
                    ball1.direction=atan2(ball1.yv,ball1.xv);
                    ball1.speed=sqrt(pow(ball1.xv,2)+pow(ball1.yv,2));
                    ball2.direction=atan2(ball2.yv,ball2.xv);
                    ball2.speed=sqrt(pow(ball2.xv,2)+pow(ball2.yv,2));
                    var collisionAngle=atan2(ball1.y-ball2.y,ball1.x-ball2.x);
                    var a1=(ball1.speed*cos(ball1.direction-collisionAngle)*(ball1.mass-ball2.mass)+2*ball2.mass*ball2.speed*cos(ball2.direction-collisionAngle))/(ball1.mass+ball2.mass);
                    var b1=ball1.speed*sin(ball1.direction-collisionAngle);
                    var a2=(ball2.speed*cos(ball2.direction-collisionAngle)*(ball2.mass-ball1.mass)+2*ball1.mass*ball1.speed*cos(ball1.direction-collisionAngle))/(ball2.mass+ball1.mass);
                    var b2=ball2.speed*sin(ball2.direction-collisionAngle);
                    var xv1=a1*cos(collisionAngle)+b1*cos(collisionAngle+90);
                    var yv1=a1*sin(collisionAngle)+b1*sin(collisionAngle+90);
                    var xv2=a2*cos(collisionAngle)+b2*cos(collisionAngle+90);
                    var yv2=a2*sin(collisionAngle)+b2*sin(collisionAngle+90);
                    ball1.xv=xv1;
                    ball2.xv=xv2;
                    ball1.yv=yv1;
                    ball2.yv=yv2;
                    collide[j][i]=1;
                    collide[i][j]=1;
                }
            } else if (sqrt(pow((balls[i].x-ball1.x),2)+pow((balls[i].y-ball1.y),2))>(balls[i].siz/2+ball1.siz/2)){
                    collide[j][i]=0;
                    collide[i][j]=0;
            }
        }
    }
};
var moveBalls = function(){
    for (var i=0;i<balls.length;i++){
        collision(i);
        bounce(balls[i]);
        balls[i].yv+=sin(gravity.direction)*gravity.strength;
        balls[i].xv+=cos(gravity.direction)*gravity.strength;
        // balls[i].direction=atan2(balls[i].yv,balls[i].xv);
        // balls[i].speed=sqrt(pow(balls[i].xv,2)+pow(balls[i].yv,2));
        balls[i].x+=balls[i].xv;
        balls[i].y+=balls[i].yv;
    }
};

var KE=function(){
    var ke=0;
    for (var i=0;i<balls.length;i++){
        balls[i].speed=(pow(balls[i].xv,2)+pow(balls[i].yv,2));
        ke+=balls[i].mass*balls[i].speed/2;
    }
    return ke;
};

var PE=function(){
    var pe=0;
    var corner={x:0,y:0};
    switch (floor(gravity.direction/90)){
        case 0: corner.x=400; corner.y=400; break;
        case 1: corner.x=0; corner.y=400; break;
        case 2: corner.x=0; corner.y=0; break;
        case 3: corner.x=4000; corner.y=10; break;
    }
    for (var i=0;i<balls.length;i++){
        var theta=atan2((corner.y-balls[i].y),(corner.x-balls[i].x))-gravity.direction;
        var PEdistance=cos(theta)*sqrt(pow((balls[i].x-corner.x),2)+pow((balls[i].y-corner.y),2));
        // PEdistance=balls[i].y;
        pe+=balls[i].mass*gravity.strength*PEdistance;
    }
    return pe;
};

var massCenter=function(){
    var massX=0;
    var massY=0;
    var massTotal=0;
    for (var i=0;i<balls.length;i++){
        massX+=balls[i].x*balls[i].mass;
        massY+=balls[i].y*balls[i].mass;
        massTotal+=balls[i].mass;
    }
    // var massAverage=massTotal/balls.length;
    massX=massX/massTotal;
    massY=massY/massTotal;
    fill(0,0,255);
    strokeWeight(2.5);
    stroke(255,250,50);
    ellipse(massX,400-massY,30,30);
    fill(0,255,0);
    text("M",massX-5,400-massY+4);
    noStroke();
    fill(255,0,0);
    // text("PE: "+massY*massTotal*gravity.strength,5,26.5);
    // text("E: "+(KE()+massY*massTotal*gravity.strength),5,40);
};

var idealPressure=function(i){
    var TempNum=0;
    for (var i=0;i<balls.length;i++){
        TempNum+=balls[i].speed;
    }
    return R*TempNum/volume;
};
// newBall(300,300,20,color(25,100,250));
// newBall(100,150,20,color(21, 189, 26));
for (var i=0;i<50;i++){
    var s=40;
    newBall(random(400-s*3)+s*3/2,random(400-s*3)+s*3/2,s,color(random(255),random(255),random(255)));
    var nun=[];
    for (var j=0;j<10;j++){
        nun.push(0);
    }
    collide.push(nun);
}
// println(gravity.direction);
var draw = function() {
    gravity.direction=(gravity.direction+(0.2))%(360);
    backg();
    drawBalls();
    stroke(255, 0, 0);
    strokeWeight(1);
    line(200,200,200+cos(gravity.direction)*1000*gravity.strength,200-sin(gravity.direction)*1000*gravity.strength);
    noStroke();
    fill(17, 255, 0);
    text("KE: "+KE(),5,13);
    text("E: "+(KE()+PE()),5,40);
    fill(217, 31, 31);
    text("PE: "+PE(),5,26.5);
    text("Pressure: "+pressure,5,53.5);
    text("Ideal Pressure: "+idealPressure(),5,67);
    pressure+=collisions[timer];
    timer=(timer+1)%pressures;
    pressure-=collisions[timer];
    collisions[timer]=0;
    massCenter();
    moveBalls();
};
