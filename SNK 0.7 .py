# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 08:52:45 2022

@author: info
"""
from turtle import *
import turtle
reset()
getscreen().bgcolor("#f1f1f1")

title("LOGO NEO GEO par Lucas Morel")
pencolor("black")
width(10)
speed(20)
color("black")
pu()
goto(0,0)
pd()

begin_fill()
circle(190)
end_fill()

goto(-140,210)

pencolor("#ffc011")
width(1)
begin_fill()
fillcolor("#ffc011")
left(90)
forward(90)
right(40)
forward(25)
right(80)
forward(70)
left(110)
forward(60)
right(160)
forward(22)
left(150)
forward(20)
right(150)
forward(20)
left(150)
forward(15)
right(160)
forward(115)
right(120)
forward(80)
left(90)
forward(75)
right(150)
forward(20)
end_fill()

pu()


goto(-25,190)

#Lettre E jaune
pd()
begin_fill()
forward(140)
right(75)
forward(70)
right(160)
forward(15)
left(155)
forward(15)
right(160)
forward(20)
left(160)
forward(20)
right(160)
forward(65)
left(150)
forward(60)
right(140)
forward(80)
left(50)
forward(15)
left(100)
forward(55)
right(150)
forward(10)
left(145)
forward(10)
right(150)
forward(10)
left(145)
forward(10)
right(148)
forward(80)
end_fill()
pu()

goto(80,290)

#Lettre O jaune
pd()
begin_fill()
left(30)
forward(40)
left(50)
forward(50)
left(10)
forward(40)
left(40)
forward(25)
left(70)
forward(50)
left(45)
forward(30)
left(30)
forward(65)
left(38)
forward(30)
end_fill()
pu()
#LETTRE JAUNE FINI

goto(-50,180)

#G

pd()
pencolor("#00a2e7")
fillcolor("#00a2e7")
begin_fill()
turtle.circle(70,170)
forward(70)
left(130)
forward(100)
left(100)
forward(50)
left(170)
forward(18)
right(160)
forward(20)
left(150)
forward(20)
right(160)
forward(20)
left(160)
forward(20)
right(80)
forward(20)
left(80)
turtle.circle(40,-200)
left(180)
forward(40)
end_fill()
pu()




#E 2
goto(30,100)
pd()
begin_fill()
left(135)
forward(55)
right(140)
forward(50)
left(160)
forward(20)
right(155)
forward(25)
left(150)
forward(30)
right(150)
forward(15)
left(155)
forward(64)
left(106)
forward(113)
left(60)
forward(73)
left(168)
forward(15)
right(160)
forward(15)
left(150)
forward(15)
right(150)
forward(15)
left(158)
forward(60)
end_fill()
pu()



#O 2
goto(55,90)
pd()

right(50)
forward(-20)
begin_fill()
forward(80)
right(63)
forward(55)
right(91)
forward(48)
right(40)
forward(67)
right(30)
forward(40)
right(60)
forward(20)
end_fill()
pu()

speed(4)


#visages
pencolor("black")
fillcolor("black")
begin_fill()
goto(62,55)
pd()
right(40)
forward(15)
right(40)
forward(10)
right(50)
forward(10)
right(83)
forward(12)
left(50)
forward(7)
left(50)
forward(10)
right(90)
forward(16)
right(95)
forward(18)
right(20)
forward(7)
right(45)
forward(7)
end_fill()



#boucle infinie pour test
a=1
while 1==1:
    a+=1
    a-=1