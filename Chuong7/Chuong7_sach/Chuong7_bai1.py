import turtle as t

# --- Ngôi sao ---
t.penup()
t.goto(-200, 100)
t.pendown()
t.color("black")

for i in range(5):
    t.forward(120)
    t.right(144)

# --- Lục giác đều ---
t.penup()
t.goto(50, 100)
t.pendown()

for i in range(6):
    t.forward(80)
    t.right(60)

# --- Ma trận dấu chấm ---
t.penup()
t.goto(-100, -100)

for i in range(10):
    for j in range(10):
        t.dot(8)
        t.forward(20)
    t.backward(200)
    t.right(90)
    t.forward(20)
    t.left(90)

t.done()
