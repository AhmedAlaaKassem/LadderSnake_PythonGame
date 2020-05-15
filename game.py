from tkinter import *
from PIL import ImageTk, Image
import time
#modified in centos

STEP = 50
MARGIN = 8
START_X = 0
START_Y = 450
Dicefiles = ["null","./data/play1.png","./data/play2.png",
                    "./data/play3.png","./data/play4.png",
                    "./data/play5.png","./data/play6.png"]


def display_dice(dice_no,operation):
    if operation == "Create":
        dice = ImageTk.PhotoImage(file= Dicefiles[dice_no])
        diceimage = canvas.create_image(560, 150, anchor=NW, image=dice)
        canvas.image = dice

    elif operation == "Delete":
        canvas.delete(diceimage)

def reset():
	#Player1.player_shift(Player1.check_position())
	shiftplayer2(Player1.check_position())
	
        #canvas.move(image, STEP , 0)


def moveitem(dir):
    if dir == "Right":
        canvas.move(image, STEP, 0)
    elif dir == "Left":
        canvas.move(image, -STEP, 0)
    elif dir == "Up":
        canvas.move(image, 0, -STEP)
    elif dir == "Down":
    	canvas.move(image, 0, STEP)
    

def moveplayer(steps):
    for x in  range(steps):
        if Player1.check_position() >= 0 and Player1.check_position() <= 9 \
                or Player1.check_position() >= 21 and Player1.check_position() <= 29 \
                    or Player1.check_position() >= 41 and Player1.check_position() <= 49 \
                        or Player1.check_position() >= 61 and Player1.check_position() <= 69 \
                            or Player1.check_position() >= 81 and Player1.check_position() <= 89 :
            moveitem("Right")
            Player1.player_step(1)
            root.update()
            time.sleep(.3)

        elif Player1.check_position() % 10 == 0 :
            moveitem("Up")
            Player1.player_step(1)
            root.update()
            time.sleep(.3)
        else :
            moveitem("Left")
            Player1.player_step(1)
            root.update()
            time.sleep(.3)

def shiftplayer(steps):
    for x in  range(steps):
        if Player1.check_position() >= 0 and Player1.check_position() <= 9 \
                or Player1.check_position() >= 21 and Player1.check_position() <= 29 \
                    or Player1.check_position() >= 41 and Player1.check_position() <= 49 \
                        or Player1.check_position() >= 61 and Player1.check_position() <= 69 \
                            or Player1.check_position() >= 81 and Player1.check_position() <= 89 :
            Player1.player_step(1)
            moveitem("Right")
            

        elif Player1.check_position() % 10 == 0 :
            Player1.player_step(1)
            moveitem("Up")
            

        else :
            Player1.player_step(1)
            moveitem("Left")
            


def shiftplayer2(steps):
    for x in  range(steps):
        if Player1.check_position() >= 0 and Player1.check_position() <= 10 \
                or Player1.check_position() >= 22 and Player1.check_position() <= 30 \
                    or Player1.check_position() >= 42 and Player1.check_position() <= 50 \
                        or Player1.check_position() >= 62 and Player1.check_position() <= 70 \
                            or Player1.check_position() >= 82 and Player1.check_position() <= 90 :
            moveitem("Left")
            Player1.player_step(-1)

        elif (Player1.check_position()-1) % 10 == 0 :
            moveitem("Down")
            Player1.player_step(-1)

        else :
            moveitem("Right")
            Player1.player_step(-1)




def jumb():
    theDice.gen_dice()
    display_dice(theDice.get_dicevalue(), "Create")
    print(f"your old position is : {Player1.check_position()}")
    print(f"the dice is :{theDice.get_dicevalue()} ")
    moveplayer(theDice.get_dicevalue())


    print(f"your  position after the dice : {Player1.check_position()}")

    for element in ladders_snakes:
        if Player1.check_position() == element.check_obj():
            if (Player1.check_position() - element.get_end_point() ) < 0 :
                shiftplayer(element.get_end_point() - Player1.check_position())
            else:
            	shiftplayer2(Player1.check_position() - element.get_end_point())


                #Player1.player_shift(element.get_end_point())



            print("snakeladder")

    print(f"your position after checking ladders/snakes : {Player1.check_position()}")
    if Player1.check_position() >= 100:
        print("Player1 Win >>>")
        reset()


def move(event):
    """Move the sprite image with a d w and s when click them"""
    if event.char == "a":
        canvas.move(image, -STEP, 0)
    elif event.char == "d":
        canvas.move(image, STEP, 0)
    elif event.char == "w":
        canvas.move(image, 0, -STEP)
    elif event.char == "s":
        canvas.move(image, 0, STEP)


class Player:
    # constructor / init
    def __init__(self, name, number):
        self.__name = name
        self.__id = number
        self.__position = 0

    # Function for moving the player by steps
    def player_step(self, steps):
        self.__position += steps

    # Function used by the ladder and snakes to shift player
    def player_shift(self, shift):
        self.__position = shift

    def check_position(self):
        return self.__position


class Dice:
    def __init__(self):
        import random
        self.__DiceValue = random.randint(1, 6)

    def gen_dice(self):
        import random
        self.__DiceValue = random.randint(1, 6)

    def get_dicevalue(self):
        return self.__DiceValue


class Ladder_Snake_Obj:
    def __init__(self, start, end, type):
        self.__start = start
        self.__end = end
        self.__type = type

    def check_obj(self):
        if self.__type == "Ladder":
            return self.__start
        else:
            return self.__end

    def get_end_point(self):
        if self.__type == "Ladder":
            return self.__end
        else:
            return self.__start




# Create the window with the Tk class
root = Tk()



# Create the canvas and make it visible with pack()
canvas = Canvas(root, width=730, height=500)
canvas.pack()  # this makes it visible



welcomelable = Label(root, text="Welcome to SnakeLadder Game", font='Helvetica 18 bold')
#welcomelable.place(x=0, y=0)

buttondice = Button(root, text='Exit Game', bd='10', command=root.destroy)
buttondice.place(x=560, y=400)

b = Button(text="    Play     ", bd='10', command=jumb)
b.place(x=560, y=50)

c = Button(text="    Reset     ", bd='10', command=reset)
c.place(x=560, y=100)



# Loads and create image (put the image in the folder)
bg = ImageTk.PhotoImage(file="./data/pic.png")
background = canvas.create_image(50, 0, anchor=NW, image=bg)

img = ImageTk.PhotoImage(file="./data/player.png")
image = canvas.create_image(MARGIN + START_X, MARGIN + START_Y, anchor=NW, image=img)





# This bind window to keys so that move is called when you press a key
#root.bind("<Key>", move)


# Init system
Player1 = Player("ahmed", 1)
theDice = Dice()
ladders_snakes = []
ladders_snakes.append(Ladder_Snake_Obj(1, 38, "Ladder"))
ladders_snakes.append(Ladder_Snake_Obj(4, 14, "Ladder"))
ladders_snakes.append(Ladder_Snake_Obj(8, 30, "Ladder"))
ladders_snakes.append(Ladder_Snake_Obj(21, 42, "Ladder"))
ladders_snakes.append(Ladder_Snake_Obj(28, 76, "Ladder"))
ladders_snakes.append(Ladder_Snake_Obj(50, 67, "Ladder"))
ladders_snakes.append(Ladder_Snake_Obj(71, 92, "Ladder"))
ladders_snakes.append(Ladder_Snake_Obj(80, 99, "Ladder"))
ladders_snakes.append(Ladder_Snake_Obj(6, 36, "Snake"))
ladders_snakes.append(Ladder_Snake_Obj(10, 32, "Snake"))
ladders_snakes.append(Ladder_Snake_Obj(26, 48, "Snake"))
ladders_snakes.append(Ladder_Snake_Obj(18, 62, "Snake"))
ladders_snakes.append(Ladder_Snake_Obj(24, 88, "Snake"))
ladders_snakes.append(Ladder_Snake_Obj(56, 95, "Snake"))
ladders_snakes.append(Ladder_Snake_Obj(78, 97, "Snake"))

# this creates the loop that makes the window stay 'active'
root.mainloop()





