import os
import chucklib.chucknorris
from gtts import gTTS

goodjoke = chucklib.chucknorris.joke()

message = gTTS(goodjoke)
message.save("joke.mp3")

os.system('afplay joke.mp3')
print(goodjoke)
