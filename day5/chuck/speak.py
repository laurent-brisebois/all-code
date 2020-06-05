import os
from gtts import gTTS
# https://gtts.readthedocs.io/en/latest/index.html

message = gTTS("Luke, I am your father")
message.save("luke.mp3")
os.system('afplay luke.mp3')
