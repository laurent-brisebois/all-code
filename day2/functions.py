### -------------------------------- ###
### 2.2.1 functions with no parameters
### -------------------------------- ###

# def greetings():
#     message = "Hello, there"
#     print(message)

# greetings()





### -------------------------------- ###
### 2.2.2 functions with parameters
### -------------------------------- ###

# def greetings(name):
#     message = "Hello, " + name + "!"
#     print(message)


# greetings("Laurent")





### -------------------------------- ###
### 2.2.3 functions with default parameters
### -------------------------------- ###

x = 200

def shout_game_stats(playername, score=100):
    # entry = "Player " + playername + " scored " + str(score) + "!!!"
    # print(entry)
    print(playername)
    print(score)

shout_game_stats("Jonathan", 7)
shout_game_stats("Laurent")
