# import modules necessary for the game
import random
import curses


# intialize the curses libarary to create our screen

screen = curses.initscr()
# hide the mouse cursor
curses.curs_set(0)
# getmax screen width and hide
screen_height , screen_width = screen.getmaxyx()


# create a new window
window = curses.newwin(screen_height,screen_width,0,0)
# allow window to recive input from the keyboard
window.keypad(1)
# set the delay for updating the screen
window.timeout(100)
# set x,y coordinates of the intial position
snk_x = screen_width // 4
snk_y =  screen_height // 2
# define the intial position of the snake body

snake = [
  [snk_y,snk_x],
  [snk_y,snk_x-1],
  [snk_y,snk_x-2]
]
# create the food in the middle of window 

food = [screen_height  //2 , screen_width //2]

# add the food using PI character frim curses module
window.addch(food[0],food[1],'*')

# set intial movement direction to the right
key = curses.KEY_RIGHT
# create game loop that loops forever until player loses or quit 
while True :
  # get the next key that will be pressed by user
  next_key = window.getch()
# if user dosenot input anything , key remain same , else key will be set to the new pressed key
  key = key if next_key == -1 else next_key
# check if snake collided with the wall or itself
# if it collideds close the window & exit the program
  if snake[0][0] in [0 , screen_height] or snake[0][1] in [0,screen_width] or snake[0] in snake[1:] :
    curses.endwin() # closing the window
    quit() # exit the program
    
# set new position of the snake head based on the direction
  new_head = [snake[0][0] , snake[0][1]]

  if key == curses.KEY_DOWN:
    new_head[0]+=1
  if key == curses.KEY_UP:
    new_head[0]-=1
  if key == curses.KEY_RIGHT:
    new_head[1]+=1
  if key == curses.KEY_LEFT:
    new_head[1]-=1
# insert new head to the first position of snake list
  snake.insert(0,new_head)
# check if snake ate the food
  if snake[0] == food:
    food = None # remove food if snake ate it
    # while food is removed , generate new food in a random place on screen
    while food is None:
      new_food = [
        random.randint(1 , screen_height - 1),
        random.randint(1 , screen_width - 1),
        
      ]
      food = new_food if new_food not in snake else None
    # set the food to new food if new food generated is not in snake body and add it to         screen  
    window.addch(food[0],food[1],curses.ACS_PI)
# otherwise remove the last segment of snake body
  else:
    tail = snake.pop()
    window.addch(tail[0], tail[1],' ')

  window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
# update the position of the snake in the screen 