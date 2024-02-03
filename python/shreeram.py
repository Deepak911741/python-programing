# turtle module ko import krna
from turtle import* 
# title ka naam kya dena chahte ho
title('Jai Shree Ram')
# background color kya dena chahte ho
bgcolor('black')
# pen ka size kitna rakhna chahte ho
pensize(5)
# pen ka color kya rakhna chahte ho
pencolor("orange")
# draw 49 bar circle me Jai Shree Ram
Ram_naam = ["जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम"]
# 360 angle ko set karna
angle = 360/49
penup()
sety(-1)
for i in range(50):
    left(angle)
    forward(260)
    write(Ram_naam[i], align="right",
    font=('Arial',12,"bold"))
    backward(260)

# circle k bick me ram naam
penup()    
goto(-40,-20)
pendown()
write("|| राम ||", font=("Arial", 60,
"normal"), align="center")
hideturtle()
done()