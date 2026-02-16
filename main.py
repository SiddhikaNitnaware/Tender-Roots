# main.py

class Garden:
    def __init__(self):
        self.plants = []
        self.particles = []
    
    def add_plant(self, plant):
        self.plants.append(plant)
    
    def add_particle(self, particle):
        self.particles.append(particle)

    def water_plants(self):
        for plant in self.plants:
            plant.grow()

class Plant:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def grow(self):
        self.health += 1
        print(f"{self.name} has grown! Health: {self.health}")

class Particle:
    def __init__(self, type):
        self.type = type

    def animate(self):
        print(f"Animating {self.type} particle.")

class SoundManager:
    def play_sound(self, sound_file):
        print(f"Playing sound: {sound_file}")

# Example of using the classes
if __name__ == "__main__":
    garden = Garden()
    plant1 = Plant("Sunflower")
    garden.add_plant(plant1)
    garden.water_plants()

    particle = Particle("Rain")
    garden.add_particle(particle)
    particle.animate()

    sound_manager = SoundManager()
    sound_manager.play_sound("water.mp3")
