background(228, 153, 240);
var gravity={direction:270, strength:0};
var friction=0;
var pressure=0;
var pressures=200;
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
    mass:siz*density,
    color:color,
    xv:0,
    yv:0,
    v:[0,0]
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
        if (ball.xv>-0.3){
            ball.xv=-0.3;
        }
    }
    if (ball.x-ball.siz/2<0){
        ball.x=0+ball.siz/2;
        collisions[timer]-=ball.mass*ball.xv;
        ball.xv=abs(ball.xv)-friction;
        if (ball.xv<0.3){
            ball.xv=0.3;
        }
    }
    if (ball.y+ball.siz/2>400){
        ball.y=400-ball.siz/2;
        collisions[timer]+=ball.mass*ball.yv;
        ball.yv=-(abs(ball.yv)-friction);
        if (ball.yv>-0.3){
            ball.yv=-0.3;
        }
    }
    if (ball.y-ball.siz/2<0){
        ball.y=0+ball.siz/2;
        collisions[timer]-=ball.mass*ball.xv;
        ball.yv=abs(ball.yv)-friction;
        if (ball.yv<0.3){
            ball.yv=0.3;
        }
    }
};

var collide=[];
var collision=function(j){
    var ball1=balls[j];
    for (var i=0;i<balls.length;i++){
        if (sqrt(pow((balls[i].x-ball1.x),2)+pow((balls[i].y-ball1.y),2))>balls[i].siz/2+ball1.siz/2){
            collide[j][i]=0;
        } else{
        if (collide[j][i]===0){
        if (balls[i]===ball1){return;}
        if (sqrt(pow((balls[i].x-ball1.x),2)+pow((balls[i].y-ball1.y),2))<=balls[i].siz/2+ball1.siz/2){
            var ball2=balls[i];
            var xv1=(ball1.mass*ball1.xv-ball2.mass*ball1.xv+2*ball2.mass*ball2.xv)/(ball1.mass+ball2.mass);
            var xv2=(ball2.mass*ball2.xv-ball1.mass*ball2.xv+2*ball1.mass*ball1.xv)/(ball2.mass+ball1.mass);
            var yv1=(ball1.mass*ball1.yv-ball2.mass*ball1.yv+2*ball2.mass*ball2.yv)/(ball1.mass+ball2.mass);
            var yv2=(ball2.mass*ball2.yv-ball1.mass*ball2.yv+2*ball1.mass*ball1.yv)/(ball2.mass+ball1.mass);
            ball1.xv=xv1;
            ball2.xv=xv2;
            ball1.yv=yv1;
            ball2.yv=yv2;
            collide[j][i]=1;
            }}
        }
    }
};

var moveBalls = function(){
    for (var i=0;i<balls.length;i++){
        collision(i);
        bounce(balls[i]);
        balls[i].yv+=sin(gravity.direction)*gravity.strength;
        balls[i].xv+=cos(gravity.direction)*gravity.strength;
        balls[i].x+=balls[i].xv;
        balls[i].y+=balls[i].yv;
    }
};

var KE=function(){
    var ke=0;
    for (var i=0;i<balls.length;i++){
        ke+=balls[i].mass*(pow(balls[i].xv,2)+pow(balls[i].yv,2));
    }
    return ke;
};

// newBall(300,300,20,color(25,100,250));
// newBall(100,150,20,color(21, 189, 26));
for (var i=0;i<2;i++){
    var s=random(50);
    newBall(random(400-s*3)+s*3/2,random(400-s*3)+s*3/2,s,color(random(255),random(255),random(255)));
    collide.push([]);
}

var draw = function() {
    gravity.direction+=1;
    backg();
    drawBalls();
    moveBalls();
    stroke(255, 0, 0);
    line(200,200,200+cos(gravity.direction)*100,200-sin(gravity.direction)*100);
    stroke(0);
    fill(17, 255, 0);
    text(KE(),5,15);
    fill(0, 255, 204);
    text(pressure,5,30);
    pressure+=collisions[timer];
    timer=(timer+1)%pressures;
    pressure-=collisions[timer];
    collisions[timer]=0;
};
