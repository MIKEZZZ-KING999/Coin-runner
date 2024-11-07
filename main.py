import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

runner = Actor("runner")
runner.pos = 100,100

coin = Actor("coin")
coin.pos = 200,200

def draw():
    screen.blit("background", (0,0))
    coin.draw()
    runner.draw()
    screen.draw.text("Score: "+ str(score), color="black", topleft=(10,10))

    if game_over:
            screen.fill("red")
            screen.draw.text("Time's Up! Your Final Score: " + str(score), midtop=(WIDTH/2,10),
            fontsize=40, color="white")        

def place_coin():
      coin.x = randint(70 , (WIDTH - 70))
      coin.y = randint(70 , (HEIGHT - 70))

def time_up():
      global game_over
      game_over = True

def update():
      global score      

      if keyboard.left:
          runner.x = runner.x - 2
      if keyboard.right:
          runner.x = runner.x + 2      
      if keyboard.up:
          runner.y = runner.y - 2
      if keyboard.down:
          runner.y = runner.y + 2      

      coin_collected = runner.colliderect(coin)

      if coin_collected:    
         score = score + 10
         place_coin()

clock.schedule(time_up, 60.0)
         
pgzrun.go()

