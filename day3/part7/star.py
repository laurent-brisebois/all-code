# 3.7.1: importing and using a object
import jedi_package.jedi_module

Yoda = jedi_package.jedi_module.Jedi("Yoda", lightsaber="green", padawan=False)
Luke = jedi_package.jedi_module.Jedi("Luke", "green")
print(Yoda.lightsaber)
print(type(Yoda))
Yoda.not_the_droids("rocks")



# 3.7.2: different import statement
from jedi_package import jedi_module

DarthVader = jedi_module.Jedi(lightsaber="red", name="Darth Vader")
DarthVader.not_the_droids("troops")



# # 3.7.3: one more import statement
from jedi_package.jedi_module import Jedi

ObiWan = Jedi("Obi-Wan", "blue", padawan=False)
ObiWan.not_the_droids("computers")
