import turtle


def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font=("Times New Roman", 16, "bold"))
    t.right(90)

    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


intlist = []

for i in range(10):
    number = int(input("데이터를 입력하세요:"))
    intlist.append(number)


t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)


colorlist = ['yellow', 'navy', 'red', 'orange', 'green',
             'blue', 'skyblue', 'purple', 'violet', 'pink']


for d in intlist:
    t.color()
    drawBar(d)
