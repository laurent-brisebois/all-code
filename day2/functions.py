### -------------------------------- ###
### 2.2.1 functions with no parameters
### -------------------------------- ###

def greetings():
    message = "Hello, there"
    print(message)

greetings()





### -------------------------------- ###
### 2.2.2 functions with parameters
### -------------------------------- ###

def greetings(name):
    message = "Hello, " + name + "!"
    print(message)


greetings("Laurent")





### -------------------------------- ###
### 2.2.3 functions with default parameters
### -------------------------------- ###

def shout_game_stats(playername, score=0):
    entry = "Player " + playername + " scored " + str(score) + "!!!"
    print(entry)

shout_game_stats("Jonathan", 7)
shout_game_stats("Laurent")

