import turtle

t= turtle.Turtle ('turtle')

t.fillcolor ('orange')
t.begin_fill ()

t.width (3)
t.forward (100)
t.setheading (135)
t.forward (141.42)

t.setheading (225)
t.forward (141.42)

t.setheading (0)
t.forward (100)

t.end_fill ()

t.fillcolor ('skyblue')
t.begin_fill ()

t.forward (70)
t.right(90)
t.forward (150)

t.right (90)
t.forward (140)

t.right (90)
t.forward (150)
t.right (90)
t.forward (70)

t.end_fill ()

t.penup ()
t.right (90)
t.forward (150)

t.fillcolor ('brown')
t.begin_fill ()

t.pendown ()
t.right (180)
t.forward (75)
t.right (90)
t.forward (55)
t.right (90)
t.forward (75)

t.end_fill ()

