import pygame
import random
from graphics import *
import time
import pyglet
from pyglet import window                                                                                   #last part start

def wish(wishing):
    import turtle
    pygame.init()
    hemel = turtle.Turtle()
    hemel.width(8)
    hemel.color("red")
    new = turtle.getscreen()
    new.title("Birthday Game")
    hemel.speed(4)
    new.bgcolor("lightblue")
    # Hidden Work(penup)
    hemel.left(180)
    hemel.penup()
    hemel.forward(300)
    hemel.right(90)
    hemel.forward(100)
    hemel.pendown()

    # Printing H

    # start to draw
    hemel.forward(50)
    hemel.right(90)
    hemel.forward(50)
    hemel.left(90)
    hemel.forward(50)
    hemel.left(90)

    hemel.penup()
    hemel.forward(50)
    hemel.left(90)
    hemel.pendown()
    hemel.forward(50)
    hemel.left(90)
    hemel.forward(50)
    hemel.right(90)
    hemel.forward(50)

    # printing A

    hemel.penup()
    hemel.left(90)
    hemel.forward(15)
    hemel.pendown()
    hemel.left(70)
    hemel.forward(110)
    hemel.right(70)
    hemel.right(70)
    hemel.forward(110)
    hemel.left(180)
    hemel.forward(55)
    hemel.left(70)
    hemel.forward(38)
    hemel.left(70)
    hemel.penup()
    hemel.forward(55)
    hemel.left(110)

    hemel.forward(100)

    # printing P

    hemel.left(90)
    hemel.pendown()
    hemel.forward(100)
    hemel.right(90)
    hemel.forward(50)
    hemel.right(20)
    hemel.forward(20)
    hemel.right(70)
    hemel.forward(40)
    hemel.right(70)
    hemel.forward(20)
    hemel.right(20)
    hemel.forward(50)
    hemel.left(90)
    hemel.forward(50)
    hemel.left(90)
    hemel.penup()
    hemel.forward(100)

    # printing P

    hemel.left(90)
    hemel.pendown()
    hemel.forward(100)
    hemel.right(90)
    hemel.forward(50)
    hemel.right(20)
    hemel.forward(20)
    hemel.right(70)
    hemel.forward(40)
    hemel.right(70)
    hemel.forward(20)
    hemel.right(20)
    hemel.forward(50)
    hemel.left(90)
    hemel.forward(50)
    hemel.left(90)
    hemel.penup()
    hemel.forward(100)

    # printing Y

    hemel.forward(20)
    hemel.pendown()
    hemel.left(90)
    hemel.forward(50)
    hemel.left(30)
    hemel.forward(60)
    hemel.backward(60)
    hemel.right(60)
    hemel.forward(60)
    hemel.backward(60)
    hemel.left(30)

    # go to Home

    hemel.penup()
    hemel.home()

    hemel.color("blue")
    new.bgcolor("lightgreen")
    # setting second row

    hemel.backward(300)
    hemel.right(90)
    hemel.forward(60)
    hemel.left(180)

    # printing P

    hemel.pendown()
    hemel.forward(100)
    hemel.right(90)
    hemel.forward(50)
    hemel.right(20)
    hemel.forward(20)
    hemel.right(70)
    hemel.forward(40)
    hemel.right(70)
    hemel.forward(20)
    hemel.right(20)
    hemel.forward(50)
    hemel.backward(50)
    hemel.left(180)
    hemel.right(20)
    hemel.forward(20)
    hemel.right(70)
    hemel.forward(40)
    hemel.right(70)
    hemel.forward(20)
    hemel.right(20)
    hemel.forward(50)
    hemel.right(90)
    hemel.forward(10)

    # go to Home

    hemel.penup()
    hemel.home()

    # setting up

    hemel.backward(200)
    hemel.right(90)
    hemel.forward(10)
    hemel.left(90)
    hemel.pendown()
    hemel.forward(20)
    hemel.penup()
    hemel.home()

    # D

    hemel.backward(150)
    hemel.right(90)
    hemel.forward(60)
    hemel.pendown()
    hemel.backward(100)
    hemel.right(90)
    hemel.forward(10)
    hemel.backward(70)
    hemel.left(180)
    hemel.right(20)
    hemel.forward(20)
    hemel.right(70)
    hemel.forward(88)
    hemel.right(70)
    hemel.forward(20)
    hemel.right(20)
    hemel.forward(70)

    hemel.penup()
    hemel.home()

    # set up for A

    hemel.backward(50)
    hemel.right(90)
    hemel.forward(65)
    hemel.left(90)

    # printing A

    hemel.pendown()
    hemel.left(70)
    hemel.forward(110)
    hemel.right(70)
    hemel.right(70)
    hemel.forward(110)
    hemel.left(180)
    hemel.forward(55)
    hemel.left(70)
    hemel.forward(38)
    hemel.left(70)
    hemel.penup()
    hemel.forward(55)
    hemel.left(110)

    hemel.forward(100)

    # printing Y

    # printing Y

    hemel.pendown()
    hemel.left(90)
    hemel.forward(50)
    hemel.left(30)
    hemel.forward(60)
    hemel.backward(60)
    hemel.right(60)
    hemel.forward(60)
    hemel.backward(60)
    hemel.left(30)

    # go to Home

    hemel.penup()
    hemel.home()

    # settig pogition

    hemel.right(90)
    hemel.forward(215)
    hemel.right(90)
    hemel.forward(200)
    hemel.right(90)

    # color




    # design

    # design pattern
    hemel.home()
    hemel.forward(200)
    hemel.pendown()
    hemel.color("black")
    hemel.width(3)
    hemel.speed(0)

    def squre(length, angle):

        hemel.forward(length)
        hemel.right(angle)
        hemel.forward(length)
        hemel.right(angle)

        hemel.forward(length)
        hemel.right(angle)
        hemel.forward(length)
        hemel.right(angle)

    squre(80, 90)

    for i in range(36):
        hemel.right(10)
        squre(80, 90)

    turtle.hideturtle()
    style = ('Courier', 30, 'italic')
    style2 = ('Courier', 5, 'italic')
    turtle.setworldcoordinates(-10,-6,10,1.5)
    turtle.write("Hi, "+ name +".\n Hope all your wishes becomes true..!!\nThank You♥", font=style,align='center')
    turtle.hideturtle()
    time.sleep(5)
    animation = pyglet.image.load_animation('picture.gif')
    animSprite = pyglet.sprite.Sprite(animation)
    w = animSprite.width
    h = animSprite.height
    window = pyglet.window.Window(h+140, w+20, "Birthday Game")
    r,g,b,alpha = 0.5,0.5,0.8,0.5
    pyglet.gl.glClearColor(r,g,b,alpha)
    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()
    pyglet.app.run()
    time.sleep(500)


                                                                                                    #last part end

                                                                                            #fast part start

orangecolor = (255, 123, 7)
blackcolor = (0, 0, 0)
redcolor = (213, 50, 80)
greencolor = (0, 255, 0)
bluecolor = (50, 153, 213)
white = (255,255,255)
# taking name whom I want to wish
def name_in():
    win = GraphWin("Birthday Game", 1000, 800)
    win.setBackground(color_rgb(255, 255, 255))
    label = Text(Point(500,230),"Welcome to Birthday Game")
    label.setTextColor(color_rgb(0, 0, 0))
    label.setSize(25)
    label.draw(win)
    enter = Text(Point(500, 290), "Enter the name whom you want to wish..!!")
    enter.setTextColor(color_rgb(0, 0, 0))
    enter.setSize(20)
    enter.draw(win)
    input_box = Entry(Point(500, 360), 25)
    input_box.draw(win)
    label2 = Text(Point(500, 400), "Game Rule:")
    label2.setTextColor(color_rgb(0, 0, 0))
    label2.setSize(20)
    label2.draw(win)
    label3 = Text(Point(500, 440), "You have to Score at least 10 to open the gift box..!!")
    label3.setTextColor(color_rgb(0, 0, 0))
    label3.setSize(16)
    label3.draw(win)
    label4 = Text(Point(500, 680), "Developed by:")
    label4.setTextColor(color_rgb(0, 0, 0))
    label4.setSize(15)
    label4.draw(win)
    label2 = Text(Point(500, 700), "Asif Uddin Ahmed Hemel")
    label2.setTextColor(color_rgb(0, 0, 0))
    label2.setSize(15)
    label2.draw(win)
    win.getMouse()
    value = input_box.getText()
    win.close()
    return value


name = name_in()  # name is in

                                                                                                #first part end

                                                                                                #mid part start

# pygame window initialisation

pygame.init()
clock = pygame.time.Clock()



# display windows's height and weight
display_width = 1000
display_height = 720
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Birthday Game')
snake_block = 10
snake_speed = 15


# snake's structure and position
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orangecolor, [int(x[0]), int(x[1]), int(snake_block), int(snake_block)])


def snakegame():
    game_over = False
    game_end = False
    # co-ordinates of the snake
    x1 = display_width / 2
    y1 = display_height / 2
    # snake moves
    x1_change = 0
    y1_change = 0

    # defines the length of snake
    snake_list = []
    length_of_snake = 1

    # the co-ordinates of food element
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10
    while not game_over:

        while game_end == True:
            # for display the score
            score = length_of_snake - 1
            # for display try again
            if score < 10:
                dis.fill(bluecolor)
                font_style = pygame.font.SysFont("comicsansms", 35)
                mesg = font_style.render("You Lost! Wanna play again? Press 'p' ", True, white)
                dis.blit(mesg, [250,250])
                font_style = pygame.font.SysFont("comicsansms", 35)
                mesg2 = font_style.render("If you want to Quit press q", True, white)
                dis.blit(mesg2, [250,300])
            elif score >= 10:
                dis.fill(bluecolor)
                font_style = pygame.font.SysFont("comicsansms", 25)
                congo = "Congratulations You have win the game..!! Press 'o' to open the surprise box"
                mesg = font_style.render(congo, True, white)
                dis.blit(mesg, [int(display_width / 12), int(display_height / 3)])
                winner = pygame.image.load('winner.gif')
                dis.blit(winner,[500,300])
            score_font = pygame.font.SysFont("comicsansms", 55)
            result = score_font.render("Your Score: " + str(score), True, greencolor)
            dis.blit(result, [int(display_width / 3), int(display_height / 5)])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snakegame()
                if event.type == pygame.KEYDOWN and score>=10:
                    if event.key == pygame.K_o:
                        pygame.quit()
                        wish(name)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True
        # updated co-ordinates
        x1 += x1_change
        y1 += y1_change
        dis.fill(blackcolor)
        pygame.draw.rect(dis, greencolor, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_end = True
        snake(snake_block, snake_list)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = int(round(random.randrange(0, display_width - snake_block) / 10.0) * 10)
            foody = int(round(random.randrange(0, display_height - snake_block) / 10.0) * 10)
            length_of_snake += 1
        font_style2 = pygame.font.SysFont("comicsansms", 10)
        text = font_style2.render("Score: " + str(length_of_snake-1), True, white)
        dis.blit(text, [0, 0])
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()
    quit()


snakegame()
                                                                                                    #mid part end