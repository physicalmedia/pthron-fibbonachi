import turtle

a = 0
b = 1

t = turtle.Turtle()
t.speed(3)

while True:
    size = a * 4
    
    for i in range(4):
        t.forward(size)
        t.right(90)
        
    t.circle(-size, 90)
    
    c = a + b
    a = b
    b = c