import turtle
import random

#importing turtle and random (random fo the random food generating

turtle.tracer (1, 0) 

SIZE_X=650
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
#the size of the screen/boarder

turtle.penup()
#pen is automatically down

SQUARE_SIZE = 20
START_LENGTH = 2 #the length of th snake at the beginning of the game


#lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#making the snake
snake = turtle.clone()
snake.shape ("square")

turtle.hideturtle()

for i in range(START_LENGTH) :
    x_pos=snake.pos() [0]
    y_pos=snake.pos() [1]
    x_pos+=SQUARE_SIZE
    my_pos = (x_pos, y_pos)
    snake.goto(x_pos, y_pos)
    pos_list.append(my_pos)
    stamp_id=snake.stamp() 
    stamp_list.append(stamp_id)
    
UP_ARROW = "Up"
DOWN_ARROW = "Down"
LEFT_ARROW = "Left"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR = "space"

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -250



hi = turtle.clone()
hi.hideturtle()
hi.goto(-250, -250)
hi.pendown ()
hi.goto(-250 + 650,-250)
hi.goto (400, -250 + 500)
hi.goto (400-650, 250)
hi.goto (-250, 250-500)
hi.penup ()
def up() :
    global direction
    direction=UP
    print("You pressed the up key")

def down() :
    global direction
    direction=DOWN
    print("You pressed the down key")

def left() :
    global direction
    direction=LEFT
    print("You pressed the left key")

def right() :
    global direction
    direction=RIGHT
    print("You pressed the right key")

turtle.onkeypress (up, UP_ARROW)
turtle.onkeypress (down, DOWN_ARROW)
turtle.onkeypress (left, LEFT_ARROW)
turtle.onkeypress (right, RIGHT_ARROW)
turtle.listen ()


def make_food():
    min_x= int((LEFT_EDGE+SQUARE_SIZE/2)/SQUARE_SIZE)
    max_x= int((RIGHT_EDGE-SQUARE_SIZE/2)/SQUARE_SIZE)
    min_y= int((DOWN_EDGE+SQUARE_SIZE/2)/SQUARE_SIZE)
    max_y= int((UP_EDGE-SQUARE_SIZE/2)/SQUARE_SIZE)
    food_x= random.randint(min_x, max_x)*SQUARE_SIZE
    food_y= random.randint(min_y, max_y)*SQUARE_SIZE
 #   if food_pos 
    food_posi=(food_x, food_y)
    food_pos.append (food_posi)
    food.goto(food_posi)
    food_id = food.stamp()
    food_stamps.append(food_id)
   # else :
   #     make_food()

def move_snake() :
    my_pos = snake.pos()
    x_pos = my_pos [0]
    y_pos = my_pos [1]

    if direction==RIGHT:
        snake.goto (x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto (x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        snake.goto (x_pos,y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif direction==UP:
        snake.goto (x_pos,y_pos + SQUARE_SIZE)
        print("You moved up!")
    

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index (snake.pos())
        food.clearstamp (food_stamps[food_ind])
        food_pos.pop (food_ind)
        food_stamps.pop (food_ind)
        print ("you have eaten the food!")
        make_food()
    else :
        old_stamp = stamp_list.pop (0)
        snake.clearstamp (old_stamp)
        pos_list.pop (0)


    
    add_stamp = snake.stamp

    new_pos = snake.pos()
    new_x_pos = new_pos [0]
    new_y_pos = new_pos [1]

    
    if new_x_pos >= RIGHT_EDGE:
        print ("You hit the right edge! Game over!")
        quit ()
    elif new_y_pos <= LEFT_EDGE:
        print ("You hit the left edge! Game over!")
        quit ()
    elif new_x_pos <= DOWN_EDGE:
        print ("You hit the lower edge! Game over!")
        quit ()
    elif new_y_pos >= UP_EDGE:
        print ("You hit the upper edge! Game over!")
        quit ()
    elif pos_list[-1] in pos_list[:-1]:
        print ('You have eaten yourself! Game over!')
        quit()
    
    turtle.ontimer(move_snake, TIME_STEP)

    

move_snake()

turtle.register_shape ("trash.gif")
food = turtle.clone()
food.shape ("trash.gif")

food_pos = [(100, 100), (-100, 100), (-100, -100), (100, -100)]
food_stamps = []

for this_food_pos in food_pos:
    x = this_food_pos [0]
    y =  this_food_pos [1]
    food.goto(x,y)
    food_stamp = food.stamp ()
    food_stamps.append (food_stamp)



