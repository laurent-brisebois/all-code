class Jedi:

    def __init__(self, name, lightsaber, padawan=True):
        self.name = name
        self.padawan = padawan
        self.lightsaber = lightsaber
        self.believes_in_the_force = True

    def not_the_droids(self, thing):
        print(f'{self.name}: "These are not the {thing} you are looking for."')

    def change_lightsaber(self, new_colour):
        self.lightsaber = new_colour

    def not_padawan_anymore(self):
        self.padawan = False
