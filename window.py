from graphics import *
import board

PEG_RADIUS = 24

points = []
x_values = [250, 223, 277, 196, 250, 304, 169, 223, 277, 331, 142, 196, 250, 304, 358]
y_values = [54, 101, 101, 148, 148, 148, 195, 195, 195, 195, 242, 242, 242, 242, 242]
x = 0

pegs = []
labels = []
texts = []

def fillPeg(peg):
    if board.isOccupied(peg):
        pegs[peg].setFill('red')
    else:
        pegs[peg].setFill('black')
    drawLabel(peg)

def drawBoard():
    for i in range(len(board.board)):
        fillPeg(i)

def drawLabel(label):
    labels[label].undraw()
    labels[label].draw(win)

def printText(text, pos):
    texts.append(Text(Point(pos['x'], pos['y']), text))
    texts[text].undraw()
    texts[text].draw(win)

def drawWindow():
    for i in range(0, 15):
        pt = Point(x_values[i], y_values[i])
        pegs.append(Circle(pt, PEG_RADIUS))
        labels.append(Text(pt, str(i)))
        labels[i].setTextColor('white')
        labels[i].setSize(20)
    vertices = [Point(250, 1), Point(95, 269), Point(405, 269)]
    triangle = Polygon(vertices)
    triangle.setFill('#966f33')
    triangle.setOutline('black')
    triangle.draw(win)
    for i in range(0, 15):
        pegs[i].setFill('black')
        pegs[i].draw(win)
        drawLabel(i)

win = GraphWin("Peg", 500, 350)
drawWindow()
