
#fill(12,148,137);for(var x=2;x<6;x++){rect(x*50,50,25,25);}
#background(0);fill(202,173,237);text("Your 9X Muliplication Table:",20,20);for(var x=2;x<11;x++){text(9*x-9,40,20*x);}
#var a=[0,60,120];fill(115,0,255);var draw=function(){background(0,140,255);for(var x=0;x<3;x++){if(mouseIsPressed&&abs(mouseX-60*x-25)<25&&abs(mouseY*2-45)<25){a[x]=900;}rect(a[x],10,50,25);}};
import random
b=random.randint(0,170)
p=0
for i in range(4):
    a=i*60-60
    if a<b<a+50:
        p=i*10

print"Your toss of",b,"got",p,"points!"




import random
b=random.randint(0,170)
p=0
for i in range(4):
    a=i*60-60
    if a<b<a+50:
        p=i*10
print"Your toss of",b,"got",p,"points!"
