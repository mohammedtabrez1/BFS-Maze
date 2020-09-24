import turtle
import time
import sys
from collections import deque

window = turtle.Screen()
window.bgcolor('black')
window.title('Solve Maze by BFS')
window.setup(1300,700)

#lists
walls = []
path = []
visited = set()
queue = deque()
solution = {}  

#Global variable
start_x,start_y,end_x,end_y=0,0,0,0

grid = [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+               +s                                +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+           +                 +               ++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +       +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + + + +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++  ++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++++  ++++++++++++++    ++    e++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]




class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('yellow')
        self.penup()
        self.speed(0)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('green')
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('red')
        self.speed(0)
        self.penup()

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('blue')
        self.speed(0)
        self.penup()

class White(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.speed(0)
        self.penup()


def setup_maze(grid):
    global start_x,start_y,end_x,end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_y = 288 - (y * 24)  
            screen_x = -588 + (x * 24)

            if character == '+':
                white.goto(screen_x,screen_y)
                white.stamp()
                walls.append((screen_x,screen_y))

            if character == ' ' or character=='e':  
                path.append((screen_x,screen_y))

            if character=='e':
                red.goto(screen_x, screen_y)       
                end_x, end_y = screen_x,screen_y     
                red.stamp()

            if character == 's':
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                green.goto(screen_x, screen_y)
                green.stamp()


def search(x,y):
    queue.append((x,y))
    solution[x,y]=x,y
    while len(queue)>0:
        x,y=queue.popleft()
        
        if (x+24,y) in path and (x+24,y) not in visited:
            cell=(x+24,y)
            queue.append(cell)
            visited.add(cell)
            solution[cell]=x,y

        if (x,y-24) in path and (x,y-24) not in visited:
            cell=(x,y-24)
            queue.append(cell)
            visited.add(cell)
            solution[cell]=x,y

        if (x-24,y) in path and (x-24,y) not in visited:
            cell=(x-24,y)
            queue.append(cell)
            visited.add(cell)
            solution[cell]=x,y

        if (x,y+24) in path and (x,y+24) not in visited:
            cell=(x,y+24)
            queue.append(cell)
            visited.add(cell)
            solution[cell]=x,y

        green.goto(x,y)
        green.stamp()
            
def backtrack():
    x,y=end_x,end_y
    blue.goto(x,y)
    blue.stamp()
    while (x,y)!=(start_x,start_y):
        try:
            blue.goto(solution[x,y])
            blue.stamp()
            x,y=solution[x,y]
        except KeyError:
            print("This maze can't be solved") 
            break     


#setting up classes
white=White()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
setup_maze(grid)
search(start_x,start_y)
backtrack()



#Exit
def exit():
    window.exitonclick()
    sys.exit()
exit()
window.mainloop()