# import from file in subdirectory
import tinymod.voice

tinymod.voice.scream("what's up dog?")



# import function directly into namespace
from tinymod.voice import scream

scream("I want ice cream")
